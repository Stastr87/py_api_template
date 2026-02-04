"""Roles of users"""

from enum import Enum


class Roles(int, Enum):
    """Roles of users"""

    ADMIN = 1
    USER = 2
