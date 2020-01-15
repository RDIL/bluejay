"""Provides users with JSON responses for errors."""


import flask
import json


def setup_error_handling(app: flask.Flask):
    """Sets up error handling."""
    for code in [401, 403, 404, 500]:
        app.register_error_handler(
            code,
            lambda err: flask.Response(
                json.dumps({
                    "status": False,
                    "code": int(str(err)[:3]),
                    "error": str(err)
                }),
                int(str(err)[:3]),
                mimetype="application/json"
            )
        )
