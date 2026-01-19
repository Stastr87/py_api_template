"""Authorization namespace"""

from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Namespace, Resource

from src.users.users import is_user_exists, save_session
from web_plugin.api_package.auth_ns.const import (
    IS_SUCCESS_FIELD,
    LOGIN_FIELD,
    MESSAGE_FIELD,
    PASSWORD_FIELD,
    TOKEN_FIELD,
)
from web_plugin.api_package.auth_ns.ns_schemas import (
    LOGIN_POST_SCHEMA,
    LOGIN_RESP_SCHEMA,
    LOGOUT_DELETE_SCHEMA,
)
from web_plugin.api_package.auth_ns.urls import (
    DELETE_LOGOUT_URL,
    POST_LOGIN_URL,
)
from web_plugin.api_package.auth_ns.utils.check_pas import check_pas
from web_plugin.api_package.exceptions.exceptions import ApiExceptions
from web_plugin.api_package.utils.errors_enum import Errors

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

        username = request.get_json().get(LOGIN_FIELD)
        password = request.get_json().get(PASSWORD_FIELD)

        # Check user if exists
        if is_user_exists(username):
            is_password_correct = check_pas(username, password)
            if is_password_correct:
                access_token = create_access_token(identity=username)
                save_session(username, access_token)
                return_body = {
                    LOGIN_FIELD: username,
                    TOKEN_FIELD: access_token,
                    IS_SUCCESS_FIELD: True,
                    MESSAGE_FIELD: None,
                }

                return return_body, 200

            if not is_password_correct:
                return_body = {
                    LOGIN_FIELD: username,
                    TOKEN_FIELD: None,
                    IS_SUCCESS_FIELD: False,
                    MESSAGE_FIELD: Errors.INVALID_PASSWORD.text(),
                }
                return return_body, 401

        if not is_user_exists(username):
            return_body = {
                LOGIN_FIELD: username,
                TOKEN_FIELD: None,
                IS_SUCCESS_FIELD: False,
                MESSAGE_FIELD: Errors.USER_NOT_FOUND.text(),
            }
            return return_body, 401

        # Как сохранять токен активной сессии пользователя?
        # Как распределять права доступа пользователей?

        return {}, 400


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
