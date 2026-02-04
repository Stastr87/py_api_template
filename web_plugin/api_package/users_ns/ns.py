"""Users namespace"""

from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource

from src.hashmap.encryption import get_salt_password_hash
from src.hashmap.password_hash_map import UserPasswordHash, UserPasswordHashMap
from src.users.roles import Roles
from src.users.users import is_token_revoked
from web_plugin.api_package.common_schemas.common_schemas import (
    COMMON_RETURN_SCHEMA,
)
from web_plugin.api_package.exceptions.exceptions import ApiExceptions
from web_plugin.api_package.users_ns.const import (
    LOGIN_FIELD,
    PASSWORD_FIELD,
    ROLE_FIELD,
)
from web_plugin.api_package.users_ns.ns_schemas import CREATE_USER_POST_SCHEMA
from web_plugin.api_package.users_ns.urls import CREATE_USER_URL
from web_plugin.api_package.utils.errors_enum import Errors

users_ns = Namespace("Users", description="Users methods")


@users_ns.route(CREATE_USER_URL)
class CreateUser(Resource):
    """HTTP method described in self doc interface swagger"""

    @jwt_required()
    @cross_origin()
    @users_ns.doc("Create a new user")
    @users_ns.expect(users_ns.model("create_user_post_schema", CREATE_USER_POST_SCHEMA))
    @users_ns.marshal_with(users_ns.model("common_return_schema", COMMON_RETURN_SCHEMA))
    def post(self) -> tuple[dict, int]:
        """request to create user in db"""

        try:
            username = request.get_json().get(LOGIN_FIELD)
            password = request.get_json().get(PASSWORD_FIELD)
            role = request.get_json().get(ROLE_FIELD)
            gwt = get_jwt()
            login = get_jwt_identity()

            if is_token_revoked(login):
                return {}, 401

            if gwt["role"] != Roles.ADMIN.value:
                raise ApiExceptions(Errors.NOT_ALLOWED.text())

            role = Roles(int(role))
            s, h = get_salt_password_hash(password)

            users_db = UserPasswordHashMap()
            users_db.load_credentials()
            users_db.put(username, UserPasswordHash(role, s, h))
            users_db.store()
            return {"msg": f"Successfully created user '{username}'", "err": False}, 200

        except ApiExceptions as err:
            return {
                "msg": f"failed to create user. Error: {err}.",
                "err": True,
            }, 400
