"""Executable point"""

from flask import Flask
from flask_cors import CORS

from api_extension import open_api

app = Flask(__name__)
open_api.init_app(app)

# allow CORS for all domains on all routes.
cors = CORS(app)

app.run("127.0.0.1", debug=True, port=5555)
