"""Default namespace openApi schemas"""

from flask_restx import fields

COMMON_RETURN_SCHEMA = {
    "msg": fields.String(),
    "err": fields.Boolean(),
}
