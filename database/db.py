import os
import sqlite3
import secrets
import hashlib
from datetime import datetime, timezone

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError, VerificationError
import sqlcipher3.dbapi2 as sqlcipher

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_DB = os.path.join(BASE_DIR, "database", "users.db")
VAULTS_DIR = os.path.join(BASE_DIR, "vaults")

os.makedirs(VAULTS_DIR, exist_ok=True)


_hasher = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=2,
    hash_len=32,
    salt_len=16
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def _vault_path(username:str) -> str:
    return os.path.join(VAULTS_DIR, f"{username}.db")

def _derive_encryption_key(master_password: str, salt: str) -> str:
    key = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=master_password.encode("utf-8"),
        salt=bytes.fromhex(salt),
        iterations=600_000
    )
    return key.hex()

def init_users_db() -> None:
    with sqlite3.connect(USERS_DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                username        TEXT NOT NULL UNIQUE,
                is_admin        INTEGER NOT NULL DEFAULT 0,
                master_hash     TEXT NOT NULL,
                kdf_salt        TEXT NOT NULL,
                enc_key_salt    TEXT NOT NULL,
                failed_attempts INTEGER NOT NULL DEFAULT 0,
                locked_until    TEXT,
                created_at      TEXT NOT NULL,
                updated_at      TEXT NOT NULL
            )
            """)
        conn.commit()

def create_user(username: str, master_password: str, is_admin: bool = False) -> dict:
    
    with sqlite3.connect(USERS_DB) as conn:
        existing = conn.execute(
            "SELECT user_id FROM users WHERE username = ?", (username,)
        ).fetchone()

    if existing:
        return {"success": False, "error": "Username already exists. Try another username."}
    
    master_hash = _hasher.hash(master_password)

    kdf_salt = secrets.token_hex(32)

    enc_key_salt = secrets.token_hex(32)

    now = _now()

    with sqlite3.connect(USERS_DB) as conn:
        conn.execute("""
            INSERT INTO users
                (username, is_admin, master_hash, kdf_salt, enc_key_salt,
                failed_attempts, locked_until, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, 0, NULL, ?, ?)
        """, (username, int(is_admin), master_hash, kdf_salt, enc_key_salt, now, now))
        conn.commit()

    _init_vault(username, master_password, enc_key_salt)

    return {"success": True, "error":None}

def authenticate_user(username: str, master_password: str) -> dict:
    
    with sqlite3.connect(USERS_DB) as conn:
        row = conn.execute("""
            SELECT user_id, master_hash, enc_key_salt,
                           failed_attempts, locked_until
            FROM users WHERE username = ?
        """, (username,)).fetchone()

    if not row:
        return {"success": False, "error": "Invalid username or password.", "enc_key_salt": None}

    user_id, master_hash, enc_key_salt, failed_attempts, locked_until = row

    if locked_until:
        lock_time = datetime.fromisoformat(locked_until)
        if datetime.now(timezone.utc) < lock_time:
            return {
                "success": False,
                "error": "Account is temporarily locked. Please try again later.",
                "enc_key_salt": None
            }
    try:
        _hasher.verify(master_hash, master_password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        _record_failed_attempts(username, user_id, failed_attempts)
        return {"success": False, "error": "Invalid username or password.", "enc_key_salt":None}
    
    with sqlite3.connect(USERS_DB) as conn:
        conn.execute("""
            UPDATE users
            SET failed_attempts = 0, locked_until = NULL, updated_at = ?
            WHERE user_id = ?
        """, (_now(), user_id))
        conn.commit()
    
    return {"success": True, "error": None, "enc_key_salt": enc_key_salt}

def _record_failed_attempts(username: str, user_id: int, current_failures: int) -> None:

    new_count = current_failures + 1
    locked_until = None

    if new_count >= 5:
        from datetime import timedelta
        locked_until = (datetime.now(timezone.utc) + timedelta(minutes=15)).isoformat()

    with sqlite3.connect(USERS_DB) as conn:
        conn.execute("""
            UPDATE users
            SET failed_attempts = ?, locked_until = ?, updated_at = ?
            WHERE user_id = ?
                     """, (new_count, locked_until, _now(), user_id))
        conn.commit()

def _init_vault(username: str, master_password: str, enc_key_salt: str) -> None:
    key = _derive_encryption_key(master_password, enc_key_salt)
    path = _vault_path(username)

    with sqlcipher.connect(path) as conn:
        conn.execute(f"PRAGMA key = \"x'{key}'\";")
        conn.execute("PRAGMA cipher_page_size = 4096;")
        conn.execute("PRAGMA kdf_iter = 64000;")
        conn.execute("PRAGMA foreign_keys = ON;")


        conn.execute("""
           CREATE TABLE IF NOT EXISTS credentials (
                credential_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                service_name       TEXT NOT NULL,
                login_username     TEXT,
                encrypted_password TEXT NOT NULL,
                encryption_iv      TEXT NOT NULL,
                created_at         TEXT NOT NULL,
                updated_at         TEXT NOT NULL
            )          
                     
            """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                audit_log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type   TEXT NOT NULL,
                event_detail TEXT,
                created_at   TEXT NOT NULL
            )             
        """)

        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS credentials_updated_at
            AFTER UPDATE ON credentials
            FOR EACH ROW
            BEGIN
                UPDATE credentials
                SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                WHERE credential_id = OLD.credential_id;
            END     

            """)
        
        conn.commit()


def open_vault(username: str, master_password: str, enc_key_salt: str):

    key = _derive_encryption_key(master_password, enc_key_salt)
    path = _vault_path(username)

    conn = sqlcipher.connect(path)
    conn.execute(f"PRAGMA key = \"x'{key}'\";")
    conn.execute("PRAGMA cipher_page_size = 4096;")
    conn.execute("PRAGMA kdf_iter = 64000;")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def add_credential(vault_conn, service_name: str, login_username:str,
                    plaintext_password: str, encryption_key: bytes) -> dict:
    from database.crypto import encrypt_password

    encrypted, iv = encrypt_password(plaintext_password, encryption_key)
    now = _now()

    vault_conn.execute("""
        INSERT INTO credentials
            (service_name, login_username, encrypted_password, encryption_iv,
            created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (service_name, login_username, encrypted, iv, now, now))
    vault_conn.commit()

    _write_audit(vault_conn, "CREDENTIAL_ADDED", f"Added entry for {service_name}")
    return {"success": True, "error": None}


def get_all_credentials(vault_conn) -> list[dict]:
    rows = vault_conn.execute("""
        SELECT credential_id, service_name, login_username,
               created_at, updated_at
        FROM credentials
        ORDER BY service_name ASC
    """).fetchall()

    return [
        {
            "credential_id": row[0],
            "service_name": row[1],
            "login_username": row[2],
            "created_at": row[3],
            "updated_at": row[4],
        }
        for row in rows
    ]

def get_credential(vault_conn, credential_id: int,
                   encryption_key: bytes) -> dict | None:
    from database.crypto import decrypt_password

    row = vault_conn.execute("""
        SELECT credential_id, service_name, login_username,
               encrypted_password, encryption_iv, created_at, updated_at
        FROM credentials WHERE credential_id = ?
    """, (credential_id,)).fetchone()

    if not row:
        return None
    

    plaintext = decrypt_password(row[3], row[4], encryption_key)

    return {
        "credential_id": row[0],
        "service_name": row[1],
        "login_username": row[2],
        "password": plaintext,
        "created_at": row[5],
        "updated_at": row[6]
    }

def update_credential(vault_conn, credential_id: int, service_name: str, login_username: str,
                      plaintext_password: str, encryption_key: bytes) -> dict:
    from database.crypto import encrypt_password

    encrypted, iv = encrypt_password(plaintext_password, encryption_key)

    vault_conn.execute("""
        UPDATE credentials
        SET service_name = ?, login_username = ?,
            encrypted_password = ?, encryption_iv = ?
        WHERE credential_id = ?
    """, (service_name, login_username, encrypted, iv, credential_id))
    vault_conn.commit()

    _write_audit(vault_conn, "CREDENTIAL_UPDATED", f"Updated entry for {service_name}")
    return {"success": True, "error": None}


def delete_credential(vault_conn, credential_id: int, service_name: str) -> dict:
    vault_conn.execute("DELETE FROM credentials WHERE credential_id = ?", (credential_id,))
    vault_conn.commit()

    _write_audit(vault_conn, "CREDENTIAL_DELETED", f"Deleted entry for {service_name}")
    return {"success": True, "error": None}


def _write_audit(vault_conn, event_type: str, event_detail: str = None) -> None:
    vault_conn.execute("""
        INSERT INTO audit_log (event_type, event_detail, created_at)
        VALUES (?, ?, ?)
    """, (event_type, event_detail, _now()))
    vault_conn.commit()

def derive_vault_key(master_password: str, enc_key_salt: str) -> bytes:
    hex_key = _derive_encryption_key(master_password, enc_key_salt)
    return bytes.fromhex(hex_key)

#1. Verify the current password against user.db
#2. Re-hash the new password and generate a fresh enc_key_salt
#3. Derive the new encryption key and call PRAGMA rekey on the vault
#file, thus re-encrypting the entire file in place with the new key.
#4. Update user.db with the new hash and new enc_key_salt

#Returns dict with 'success' (bool) and 'error' (str or None), and on success,
#'new_enc_key_salt' so the caller can update the session.
def change_master_password(username: str, current_password: str, 
                           new_password: str, vault_conn) -> dict:
    
    with sqlite3.connect(USERS_DB) as conn:
        row = conn.execute("""
            SELECT user_id, master_hash, enc_key_salt
            FROM users WHERE username = ?
                           """, (username,)).fetchone()
    if not row:
        return {"success": False, "error": "User not found.", "new_enc_key_salt": None}
    
    user_id, master_hash, old_enc_key_salt = row

    try:
        _hasher.verify(master_hash, current_password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return {"success": False, "error": "Current password is incorrect.", "new_enc_key_salt": None}
    
    new_master_hash = _hasher.hash(new_password)
    new_enc_key_salt = secrets.token_hex(32)
    new_key = _derive_encryption_key(new_password, new_enc_key_salt)

    try:
        vault_conn.execute(f"PRAGMA rekey = \"x'{new_key}'\";")
    except Exception as e:
        return {"success": False, "error": f"Vault rekey failed: {e}", "new_enc_key_salt": None}
    
    with sqlite3.connect(USERS_DB) as conn:
        conn.execute("""
            UPDATE users
            SET master_hash = ?, enc_key_salt = ?, updated_at = ?
            WHERE user_id = ?
        """, (new_master_hash, new_enc_key_salt, _now(), user_id))
        conn.commit()

    _write_audit(vault_conn, "PASSWORD_CHANGED", "Master password changed successfully!")

    return {"success": True, "error": None, "new_enc_key_salt": new_enc_key_salt}

    