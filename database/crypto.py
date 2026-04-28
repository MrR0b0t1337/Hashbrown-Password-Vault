import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_password(plaintext: str, key: bytes) -> tuple[str, str]:
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext.encode("utf-8"), None)

    return (
        base64.b64encode(ciphertext).decode("utf-8"),
        base64.b64encode(iv).decode("utf-8")
    )

def decrypt_password(encrypted_b64: str, iv_b64: str, key: bytes) -> str:
    ciphertext = base64.b64decode(encrypted_b64)
    iv = base64.b64decode(iv_b64)
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, ciphertext, None)

    return plaintext.decode("utf-8")

def derive_key_bytes(hex_key: str) -> bytes:
    return bytes.fromhex(hex_key)