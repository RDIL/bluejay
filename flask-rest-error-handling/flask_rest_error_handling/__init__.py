"""A Flask extension that provides users with JSON responses for errors."""

import flask
import json


def setup_error_handling(
    app: flask.Flask,
    error_codes=[401, 403, 404, 500],
    access_control_allow_origin: str = "*"
):
    """
    Sets up error handling.

    Parameters:
        app: The flask.Flask object to configure.
        error_codes: A list of integers or Exception subclasses to handle. (Optional)
        access_control_allow_origin:
            A string for the value of the Access-Control-Allow-Origin header.
            (this is Optional, defaults to "*", meaning any domain.)
    """

    for code in error_codes:
        app.register_error_handler(
            code,
            lambda err: flask.Response(
                json.dumps({
                    "status": False,
                    "code": _get_named_code(err),
                    "error": str(err)
                }),
                # gets the first 3 characters of the error code, e.g. 404
                _get_named_code(err),
                mimetype="application/json",
                headers={
                    "Access-Control-Allow-Origin": access_control_allow_origin
                }
            )
        )


def _get_named_code(error) -> int:
    """Gets the error code as an integer (e.g. 404) from the error string."""

    return int(str(error)[:3])
