"""Provides users with JSON responses for errors."""

import flask
import json


def setup_error_handling(
    app: flask.Flask,
    error_codes=[401, 403, 404, 500]
):
    """
    Sets up error handling.

    Parameters:
        app: The flask.Flask object to configure.
        error_codes: A list of integers or Exceptions to handle.
    """
    for code in error_codes:
        app.register_error_handler(
            code,
            lambda err: flask.Response(
                json.dumps({
                    "status": False,
                    "code": int(str(err)[:3]),
                    "error": str(err)
                }),
                # gets the first 3 characters of the error code, e.g. 404
                int(str(err)[:3]),
                mimetype="application/json"
            )
        )
