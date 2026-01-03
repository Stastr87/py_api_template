"""Init api self doc service"""

from flask_restx import Api

from web_plugin.api_package.default_ns.ns import default_ns

open_api = Api(
    version="1.0",
    title="web app template API",
    description="swagger doc service",
    doc="/swagger",
)

open_api.add_namespace(default_ns, path="/api/v1")
