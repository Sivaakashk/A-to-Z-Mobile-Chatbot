from flask import (
    Blueprint,
    jsonify,
    request,
    render_template
)

from services.phone_service import (
    PhoneService
)

from services.comparison_service import (
    ComparisonService
)


phone_bp = Blueprint(
    "phones",
    __name__,
    url_prefix="/phones"
)


@phone_bp.route("/")
def get_phones():

    phones = (
        PhoneService.get_all_phones()
    )

    return jsonify(phones)


@phone_bp.route(
    "/search"
)
def search_phone():

    query = request.args.get(
        "q",
        ""
    )

    results = (
        PhoneService.search_by_name(
            query
        )
    )

    return jsonify(results)


@phone_bp.route(
    "/<phone_id>"
)
def phone_details(phone_id):

    phone = (
        PhoneService.get_phone_by_id(
            phone_id
        )
    )

    if not phone:

        return jsonify({

            "error":
                "Phone not found"

        }), 404

    return jsonify(phone)


@phone_bp.route(
    "/compare"
)
def compare_phones():

    phone1 = request.args.get(
        "phone1"
    )

    phone2 = request.args.get(
        "phone2"
    )

    result1, result2 = (

        ComparisonService.compare(
            phone1,
            phone2
        )

    )

    if not result1 or not result2:

        return jsonify({

            "error":
                "One or both phones not found"

        }), 404


    comparison = (

        ComparisonService.create_comparison_data(

            result1,

            result2

        )

    )

    return jsonify(comparison)