"""Encryption methods for hashing passwords."""

import hashlib
import os


def hash_password_with_salt(password) -> tuple[bytes, bytes]:
    """Generate salt and hash password."""
    # Генерация случайной соли
    salt = os.urandom(32)

    # Хеширование пароля с солью
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",  # Используемый алгоритм хеширования
        password.encode("utf-8"),  # Пароль в виде байтов
        salt,  # Соль
        100000,  # Количество итераций
        dklen=128,  # Длина получаемого ключа в байтах
    )

    # Сохраняем соль вместе с хешем для последующей верификации
    return salt, password_hash


def verify_password(
    stored_salt: bytes, stored_password_hash: bytes, provided_password: str
) -> bool:
    """Verify provided password against stored password."""

    password_hash = hashlib.pbkdf2_hmac(
        "sha256", provided_password.encode("utf-8"), stored_salt, 100000, dklen=128
    )

    # Сравнение хешей

    return password_hash == stored_password_hash
