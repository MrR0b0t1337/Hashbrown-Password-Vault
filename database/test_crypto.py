import os
import sys
from cryptography.exceptions import InvalidTag

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.crypto import encrypt_password, decrypt_password, derive_key_bytes

def passed(description):
    print(f"PASS-{description}")

def failed(description, detail=""):
    print(f"FAIL-{description}")
    if detail:
        print(f"{detail}")

TEST_KEY = os.urandom(32)
print(f"\nTest key (hex value): {TEST_KEY.hex()}")

#TEST 1- Make sure we can encrypt a password, then decrypt it.

print("\nTest 1: Encrypt & Decrypt")
try:
    original = "MySecretPassword123!"
    encrypted, iv = encrypt_password(original, TEST_KEY)
    decrypted = decrypt_password(encrypted, iv, TEST_KEY)

    print(f"Original plaintext:    {original}")
    print(f"IV (base64):    {iv}")
    print(f"Ciphertext (base64):    {encrypted}")
    print(f"Decrypted plaintext:    {decrypted}")

    if decrypted == original:
        passed("Decrypted value matches original plaintext")
    else:
        failed("Decrypted value does NOT match original")
except Exception as e:
    failed("Raised and exception", str(e))

#TEST 2- When given a wrong key, the encryption algorithm should produce an error

print("\nTest 2: Wrong key raises an error")
try:
    original = "MySecretPassword123!"
    encrypted, iv = encrypt_password(original, TEST_KEY)
    wrong_key = os.urandom(32)

    print(f"Correct key (hex value):    {TEST_KEY.hex()}")
    print(f"Wrong key (hex value):    {wrong_key.hex()}")

    try:
        decrypt_password(encrypted, iv, wrong_key)
        failed("Wrong key returned bad data but no error was raised!")
    except InvalidTag:
        passed("Wrong key correctly raised an authentication error (InvalidTag)")
    except Exception as e:
        failed(f"Wrong key raised the wrong exception type: {type(e).__name__}", str(e))

except Exception as e:
    failed("Test raised an unexpected exception", str(e))

#TEST 3- Unique IV per encryption
#(Encrypting the same password twice should produce different ciphertext
#and different IVs each time, because os.urandom(12) is called fresh each time)

print("\nTest 3: Unique IV generated per encryption operation")
try:
    password = "MySecretPassword123!"
    encrypted1, iv1 = encrypt_password(password, TEST_KEY)
    encrypted2, iv2 = encrypt_password(password, TEST_KEY)

    print(f"Same password used twice:    {password}")
    print(f"Encryption 1:    {iv1}")
    print(f"Encryption 2:    {iv2}")
    print(f"Encryption 1 ciphertext:    {encrypted1}")
    print(f"Encryption 2 ciphertext:    {encrypted2}")

    if iv1 != iv2:
        passed("Two encryption operations on the same plaintext produced different IVs")
    else:
        failed("Both encryptions produced the same IV...IV is not random")
    
    if encrypted1 != encrypted2:
        passed("Two encryption operations produced different ciphertexts")
    else:
        failed("Both encryption operations produced identical ciphertext")

except Exception as e:
    failed("Test raised an exception", str(e))

#TEST 4-    y password
#Ensure the app behaves normally if a user attempts to save an entry with no password

print("\nTest 4: Empty string password")
try:
    empty = ""
    encrypted, iv = encrypt_password(empty, TEST_KEY)
    decrypted = decrypt_password(encrypted, iv, TEST_KEY)

    print(f"Empty string plaintext:    {empty}")
    print(f"IV (base64):    {iv}")
    print(f"Ciphertext (base64):    {encrypted}")
    print(f"Decrypted plaintext:    {decrypted}")

    if decrypted == empty:
        passed("Empty string encrypts and decrypts correctly")
    else:
        failed("Empty string failed")

except Exception as e:
    failed("Empty string raised an exception", str(e))

#TEST 5- Special Characters

print("\nTest 5: Special characters")
try:
    special = "P@$$w0rd!#%^&*()_+-=[]{}|;':\",./<>?"
    enc, iv = encrypt_password(special, TEST_KEY)
    dec = decrypt_password(enc, iv, TEST_KEY)

    print(f"Original:    {special}")
    print(f"IV:    {iv}")
    print(f"Ciphertext:    {enc}")
    print(f"Decrypted:    {dec}")

    if dec == special:
        passed("Special characters were preserved and caused no issues")
    else:
        failed("Special characters corrupted during encryption/decryption")

except Exception as e:
    failed("Special characters raised an exception", str(e))

#TEST 6- derive_key_bytes (Hex to bytes, back to hex)

print("\nTest 6: derive_key_bytes converts hex key correctly")
try:
    hex_key = TEST_KEY.hex()
    key_bytes = derive_key_bytes(hex_key)

    print(f"Original key bytes:    {TEST_KEY.hex()}")
    print(f"Hex string:    {hex_key}")
    print(f"Converted back:    {key_bytes.hex()}")
    print(f"Match:    {key_bytes == TEST_KEY}")

    if key_bytes == TEST_KEY:
        passed("derive_key_bytes correctly converts hex string to bytes")
    else:
        failed("derive_key_bytes produced the wrong bytes")

except Exception as e:
    failed("derive_key_bytes raised an exception", str(e))