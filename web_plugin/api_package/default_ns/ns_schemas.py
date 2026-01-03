"""Default namespace openApi schemas"""

from flask_restx import fields

HELLO_RETURN_SCHEMA = {
    "msg": fields.String(),
    "err": fields.Boolean(),
}
