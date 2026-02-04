"""error handler"""

from web_plugin.api_package.common_schemas.fields import (
    ERROR_FIELD,
    MESSAGE_FIELD,
)


def error_handler(e, http_code: int = 400, custom_text: str = "") -> tuple:
    """Catch error code for error response"""

    msg = f"{type(e).__name__} handed! Code: {e.value}. {e.text()}."
    if custom_text:
        msg += f" Stack trace {custom_text}"
    response_body = {MESSAGE_FIELD: msg, ERROR_FIELD: True}

    return response_body, http_code
