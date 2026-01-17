"""Users module"""

from datetime import datetime, timedelta

from src.hashmap.password_hash_map import UserPasswordHashMap
from src.hashmap.session_hash_map import SessionInfo, SessionInfoHashMap


def is_user_exists(user_name) -> bool:
    """Checks if a user is present in the database"""
    db = UserPasswordHashMap()
    db.restore_hash_map()
    return user_name in db


def save_session(username: str, access_token: str) -> None:
    """Saves a user's session"""

    db = SessionInfoHashMap()
    session = SessionInfo(
        username, access_token, (datetime.now() + timedelta(days=2)).isoformat()
    )
    db.put(username, session)
    db.store()
