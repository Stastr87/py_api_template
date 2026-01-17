"""Util for authentication namespace"""

from src.hashmap.encryption import verify_password
from src.hashmap.password_hash_map import UserPasswordHashMap


def check_pas(user: str, password: str) -> bool:
    """Password verification"""

    users = UserPasswordHashMap()
    users.restore_hash_map()
    user_hash_password = users.get(user)
    return verify_password(
        bytes.fromhex(str(user_hash_password.salt)),
        bytes.fromhex(str(user_hash_password.hashed_password)),
        password,
    )
