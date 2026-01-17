"""Default namespace openApi schemas"""

from flask_restx import fields

from web_plugin.api_package.auth_ns.const import (
    IS_SUCCESS_FIELD,
    LOGIN_FIELD,
    MESSAGE_FIELD,
    PASSWORD_FIELD,
    TOKEN_FIELD,
)

LOGIN_RESP_SCHEMA = {
    LOGIN_FIELD: fields.String(),
    TOKEN_FIELD: fields.String(),
    IS_SUCCESS_FIELD: fields.Boolean(),
    MESSAGE_FIELD: fields.String(),
}

LOGIN_POST_SCHEMA = {
    LOGIN_FIELD: fields.String(),
    PASSWORD_FIELD: fields.String(),
}

LOGOUT_DELETE_SCHEMA = {
    IS_SUCCESS_FIELD: fields.Boolean(),
}
