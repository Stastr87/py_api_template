"""Flask web server custom config"""

from flask import Flask


def set_custom_config(app: Flask):
    """
    Do not remove Flask params. For Enabling/Disabling params use comments
    """
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["JSON_AS_ASCII"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["RESTX_MASK_SWAGGER"] = False

    # disable "Try it Out" for all methods
    # or add some methods in list "get", "post", etc.
    # app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = []

    # specify the initial expansion state. Use values 'none', 'list' or 'full'
    app.config["SWAGGER_UI_DOC_EXPANSION"] = "none"

    # show operationId for endpoint. Useful when yaml file is source for api.
    app.config["SWAGGER_UI_OPERATION_ID"] = False

    # Show request duration in swagger UI web page
    app.config["SWAGGER_UI_REQUEST_DURATION"] = False

    # Allow exposing a global header
    app.config["RESTX_MASK_SWAGGER"] = False

    # Authorisation settings
    # Change this to a secure secret key
    app.config["JWT_SECRET_KEY"] = "lopata"
