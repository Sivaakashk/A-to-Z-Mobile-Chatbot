from flask import (
    Blueprint,
    request,
    jsonify
)

from services.gemini_service import (
    generate_response
)

from services.firebase_service import (
    save_chat,
    get_chat_history
)

from services.phone_service import (
    PhoneService
)

from services.recommendation_service import (
    RecommendationService
)

from utils.query_parser import (
    QueryParser
)


chat_bp = Blueprint(
    "chat",
    __name__,
    url_prefix="/api"
)


@chat_bp.route(
    "/chat",
    methods=["POST"]
)
def chat():

    try:

        data = request.get_json()

        message = data.get(
            "message",
            ""
        ).strip()

        user_id = data.get(
            "user_id",
            "anonymous"
        )

        if not message:

            return jsonify({

                "success": False,

                "error":
                    "Message cannot be empty"

            }), 400


        # Parse User Query
        parsed_query = (
            QueryParser.parse(message)
        )


        phone_data = []


        # Recommendation Query
        if parsed_query["intent"] == "recommend":

            phone_data = (

                RecommendationService.recommend(

                    budget=
                        parsed_query.get("budget"),

                    brand=
                        parsed_query.get("brand"),

                    purpose=
                        parsed_query.get("purpose")

                )

            )


        # Phone Search
        elif parsed_query["intent"] == "search":

            phone_data = (

                PhoneService.search_by_name(
                    parsed_query.get(
                        "phone_name",
                        message
                    )
                )

            )


        # Default
        else:

            phone_data = (
                PhoneService.get_all_phones()
            )[:10]


        # Get Chat History
        history = get_chat_history(
            user_id
        )


        # Gemini Response
        response = generate_response(

            user_message=message,

            phone_data=phone_data,

            history=history

        )


        # Save Chat
        save_chat(

            user_id=user_id,

            message=message,

            response=response

        )


        return jsonify({

            "success": True,

            "response": response,

            "phones": phone_data

        })


    except Exception as error:

        print(error)

        return jsonify({

            "success": False,

            "error":
                "Server error"

        }), 500