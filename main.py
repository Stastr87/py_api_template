"""Executable point"""

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api_extension import open_api
from env.flask_config import set_custom_config

app = Flask(__name__)
open_api.init_app(app)

# allow CORS for all domains on all routes.
cors = CORS(app)

# set custom config placed in env/flask_config.py
set_custom_config(app)
jwt = JWTManager(app)

app.run("127.0.0.1", debug=True, port=5555)
