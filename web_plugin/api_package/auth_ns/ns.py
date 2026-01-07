"""Authorization namespace"""

from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Namespace, Resource

from web_plugin.api_package.auth_ns.ns_schemas import (
    LOGIN_POST_SCHEMA,
    LOGIN_RESP_SCHEMA,
    LOGOUT_DELETE_SCHEMA,
)
from web_plugin.api_package.auth_ns.urls import (
    DELETE_LOGOUT_URL,
    POST_LOGIN_URL,
)
from web_plugin.api_package.exceptions.exceptions import ApiExceptions

auth_ns = Namespace("Authorization", description="Authorization methods")


@auth_ns.route(POST_LOGIN_URL)
class Login(Resource):
    """HTTP method described in self doc interface swagger"""

    @cross_origin()
    @auth_ns.doc("returns authorization model")
    @auth_ns.expect(auth_ns.model("login_post_schema", LOGIN_POST_SCHEMA))
    @auth_ns.marshal_with(auth_ns.model("authorization model", LOGIN_RESP_SCHEMA))
    def post(self):
        """request returns authorization token"""

        username = "Получить из тела POST запроса"

        access_token = create_access_token(identity=username)
        return_body = {"login": None, "token": access_token, "is_success": True}
        return return_body, 200

        # try:
        #     return_body = {"login": None, "tocken": None}
        #     return return_body, 200
        #
        # except ValidationError as err:
        #     print(err)
        #     return_body = {"msg": "incorrect characters were received", "err": True}
        #     return return_body, 400


@auth_ns.route(DELETE_LOGOUT_URL)
class Logout(Resource):
    """HTTP method described in self doc interface swagger"""

    @cross_origin()
    @auth_ns.doc("returns logout schema")
    @auth_ns.marshal_with(auth_ns.model("logout model", LOGOUT_DELETE_SCHEMA))
    @jwt_required()
    def delete(self):
        """request for revoking the user's token"""

        try:
            return_body = {"is_success": True}
            return return_body, 200

        except ApiExceptions as err:
            print(err)
            return_body = {"is_success": False}
            return return_body, 400
