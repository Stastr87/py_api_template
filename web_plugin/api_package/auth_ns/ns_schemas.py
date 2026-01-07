"""Default namespace openApi schemas"""

from flask_restx import fields

LOGIN_RESP_SCHEMA = {
    "login": fields.String(),
    "token": fields.String(),
    "is_success": fields.Boolean(),
}

LOGIN_POST_SCHEMA = {
    "login": fields.String(),
    "password": fields.String(),
}

LOGOUT_DELETE_SCHEMA = {
    "is_success": fields.Boolean(),
}
