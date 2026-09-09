from services.phone_service import PhoneService


class ComparisonService:

    @staticmethod
    def compare(
        phone_name_1,
        phone_name_2
    ):

        phone1_results = (
            PhoneService.search_by_name(
                phone_name_1
            )
        )

        phone2_results = (
            PhoneService.search_by_name(
                phone_name_2
            )
        )

        if not phone1_results:

            return None, None

        if not phone2_results:

            return None, None

        return (

            phone1_results[0],

            phone2_results[0]

        )


    @staticmethod
    def create_comparison_data(
        phone1,
        phone2
    ):

        return {

            "phone_1": phone1,

            "phone_2": phone2,

            "comparison": {

                "price": {

                    "phone_1":
                        phone1.get("price"),

                    "phone_2":
                        phone2.get("price")

                },

                "processor": {

                    "phone_1":
                        phone1.get(
                            "processor"
                        ),

                    "phone_2":
                        phone2.get(
                            "processor"
                        )

                },

                "battery": {

                    "phone_1":
                        phone1.get(
                            "battery"
                        ),

                    "phone_2":
                        phone2.get(
                            "battery"
                        )

                },

                "display": {

                    "phone_1":
                        phone1.get(
                            "display"
                        ),

                    "phone_2":
                        phone2.get(
                            "display"
                        )

                }

            }

        }