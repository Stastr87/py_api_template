"""Encryption methods for hashing passwords."""

import hashlib
import os


def get_salt_password_hash(password) -> tuple[bytes, bytes]:
    """Generate salt and hash password."""

    # Генерация случайной соли
    salt = os.urandom(32)

    # Хеширование пароля с солью:
    # hash_name = "sha256" - Используемый алгоритм хеширования
    # password = password.encode("utf-8") - Пароль в виде байтов
    # salt - Соль
    # iterations = 100000 - Количество итераций
    # dklen=128 - Длина получаемого ключа в байтах

    password_hash = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=salt,
        iterations=100000,
        dklen=128,
    )
    return salt, password_hash


def verify_password(
    stored_salt: bytes, stored_password_hash: bytes, provided_password: str
) -> bool:
    """Verify provided password against stored password."""

    password_hash = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=provided_password.encode("utf-8"),
        salt=stored_salt,
        iterations=100000,
        dklen=128,
    )

    return password_hash == stored_password_hash
