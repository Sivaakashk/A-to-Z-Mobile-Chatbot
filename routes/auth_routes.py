from flask import (
    Blueprint,
    request,
    jsonify
)

from services.firebase_service import (
    verify_token
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route(
    "/verify",
    methods=["POST"]
)
def verify():

    data = request.get_json()

    token = data.get("token")

    if not token:

        return jsonify({

            "success": False,

            "error":
                "Token required"

        }), 400


    user = verify_token(token)

    if not user:

        return jsonify({

            "success": False,

            "error":
                "Invalid token"

        }), 401


    return jsonify({

        "success": True,

        "user": user

    })