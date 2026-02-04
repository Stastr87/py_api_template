"""Users namespace openApi schemas"""

from flask_restx import fields

from src.users.roles import Roles
from web_plugin.api_package.users_ns.const import (
    LOGIN_FIELD,
    PASSWORD_FIELD,
    ROLE_FIELD,
)

ROLES_ENUM = (
    str({item.name: item.value for item in Roles})
    .replace(
        "{",
        "",
    )
    .replace("}", "")
)
CREATE_USER_POST_SCHEMA = {
    LOGIN_FIELD: fields.String(),
    PASSWORD_FIELD: fields.String(),
    ROLE_FIELD: fields.Integer(description=f"Possible roles in enum: {ROLES_ENUM}"),
}
