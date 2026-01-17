"""Default namespace"""

from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from web_plugin.api_package.default_ns.ns_schemas import HELLO_RETURN_SCHEMA
from web_plugin.api_package.default_ns.params_schemas import HelloParams
from web_plugin.api_package.default_ns.urls import GET_HELLO_URL

default_ns = Namespace("default", description="default namespace example")


@default_ns.route(GET_HELLO_URL)
@default_ns.doc(
    params={
        "appeal": {
            "description": "appeal to say 'hello' authorized user",
            "type": "str",
        },
    }
)
class Hello(Resource):
    """HTTP method described in self doc interface swagger"""

    @cross_origin()
    @jwt_required()
    @default_ns.doc("returns hello schema")
    @default_ns.marshal_with(default_ns.model("hello schema", HELLO_RETURN_SCHEMA))
    def get(self):
        """request returns greetings to user"""
        current_user = get_jwt_identity()
        return_msg = "Hello world!"

        try:
            # Validate request params
            request_params = HelloParams(name=request.args.get("appeal"))

            appeal = str(request_params.name).strip()
            if appeal:
                return_msg = f"Hello {appeal} {current_user}!"

            return_body = {"msg": return_msg, "err": None}
            return return_body, 200

        except ValidationError as err:
            print(err)
            return_body = {"msg": "incorrect characters were received", "err": True}
            return return_body, 400
