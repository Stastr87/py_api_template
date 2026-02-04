"""Users module"""

from datetime import datetime, timedelta

from src.hashmap.password_hash_map import UserPasswordHashMap
from src.hashmap.session_hash_map import SessionInfo, SessionInfoHashMap


def is_user_exists(user_name) -> bool:
    """Checks if a user is present in the database"""
    db = UserPasswordHashMap()
    db.load_credentials()
    return user_name in db


def save_session(username: str, access_token: str) -> None:
    """Saves a user's session"""

    db = SessionInfoHashMap()
    session = SessionInfo(
        login=username,
        token=access_token,
        expires_in=(datetime.now() + timedelta(days=2)).isoformat(),
        is_revoked=0,
    )
    db.restore_hash_map()

    if username in db:
        print(
            f"{username} is already present in the database. Update token expiration time"
        )
        db.remove(username)
        db.put(username, session)
    if username not in db:
        db.put(username, session)
    db.store()


def finish_session(username: str) -> None:
    """Revoke user's access token"""

    db = SessionInfoHashMap()
    db.restore_hash_map()
    if username in db:
        session = db.get(username)
        session.is_revoked = 1
        db.store()


def is_token_revoked(username: str) -> bool:
    """Check is token is revoked or not"""

    db = SessionInfoHashMap()
    db.restore_hash_map()
    if username in db:
        session = db.get(username)
        return bool(session.is_revoked)
    return True
