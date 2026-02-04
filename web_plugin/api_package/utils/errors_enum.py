"""Errors Enum"""

import enum


@enum.unique
class Errors(enum.IntEnum):
    """web plugin errors"""

    def __init__(self, code):
        self.code = code

    USER_NOT_FOUND = 1
    INVALID_PASSWORD = 2
    NOT_ALLOWED = 3

    def text(self) -> str:
        """return error text"""
        text = ""

        match self.code:
            case int(self.USER_NOT_FOUND):
                text = "User not found"
            case int(self.INVALID_PASSWORD):
                text = "Incorrect password"
            case int(self.NOT_ALLOWED):
                text = "not allowed for the user's access level"

        return text
