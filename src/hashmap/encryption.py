"""encryption"""

import hashlib
import os


def encryption_srt(string: str) -> bytes:
    """encrypt provided string"""

    # Create salt - a cryptographically secure random string
    # that is added to the password before it is hashed.
    salt = os.urandom(32)

    # Create hash
    hash_str = string.encode()
    hash_obj = hashlib.pbkdf2_hmac("sha256", hash_str, salt, 100000)

    # Create encrypted string
    encrypted_srt = salt + hash_obj
    return encrypted_srt


def verify_string(encrypted_str, provided_str) -> bool:
    """Returns True if the string matches the encoded string"""
    salt = encrypted_str[:32]  # Первые 32 байта — соль
    stored_hash = encrypted_str[32:]  # Остальное — хеш
    hash_obj = hashlib.pbkdf2_hmac("sha256", provided_str.encode(), salt, 100000)
    return hash_obj == stored_hash
