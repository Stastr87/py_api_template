"""Init api self doc service"""

from flask_restx import Api

from web_plugin.api_package.auth_ns.ns import auth_ns
from web_plugin.api_package.default_ns.ns import default_ns
from web_plugin.api_package.users_ns.ns import users_ns

authorizations = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Enter authorization header like this: Bearer <token>",
    }
}

open_api = Api(
    version="1.0",
    title="web app template API",
    description="swagger doc service",
    doc="/swagger",
    authorizations=authorizations,
    security="Bearer",
)


open_api.add_namespace(default_ns, path="/api/v1")
open_api.add_namespace(auth_ns, path="/api/v1")
open_api.add_namespace(users_ns, path="/api/v1")
