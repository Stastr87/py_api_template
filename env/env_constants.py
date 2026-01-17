"""Define environment params for multi OS usage"""

import os
from sys import path

APP_WORK_DIR: str = os.path.abspath(os.path.join(__file__, "../.."))
path.append(APP_WORK_DIR)

# Users storage
USERS_STORAGE = os.path.join(APP_WORK_DIR, "src", "users", "users.csv")
SESSIONS_STORAGE = os.path.join(APP_WORK_DIR, "src", "users", "sessions.csv")
