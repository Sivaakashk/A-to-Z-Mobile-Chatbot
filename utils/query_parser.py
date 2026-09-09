import re


class QueryParser:


    @staticmethod
    def parse(message):

        message_lower = message.lower()


        result = {

            "intent": "general",

            "budget": None,

            "brand": None,

            "purpose": None,

            "phone_name": None

        }


        # Detect Recommendation Intent
        recommendation_keywords = [

            "best phone",

            "recommend",

            "suggest",

            "which phone",

            "good phone"

        ]

        if any(
            keyword in message_lower
            for keyword
            in recommendation_keywords
        ):

            result["intent"] = "recommend"


        # Detect Budget
        budget_pattern = (

            r"(?:under|below|within)"
            r"\s*(?:rs\.?|₹)?\s*"
            r"([\d,]+)"
        )

        match = re.search(

            budget_pattern,

            message_lower

        )

        if match:

            budget = (

                match.group(1)
                .replace(",", "")

            )

            result["budget"] = int(
                budget
            )


        # Detect Purpose
        if "gaming" in message_lower:

            result["purpose"] = "gaming"

            result["intent"] = "recommend"


        elif (
            "camera" in message_lower
            or "photography" in message_lower
        ):

            result["purpose"] = "camera"

            result["intent"] = "recommend"


        elif "battery" in message_lower:

            result["purpose"] = "battery"

            result["intent"] = "recommend"


        elif "display" in message_lower:

            result["purpose"] = "display"


        # Detect Brands
        brands = [

            "samsung",

            "apple",

            "iphone",

            "oneplus",

            "xiaomi",

            "redmi",

            "poco",

            "realme",

            "vivo",

            "oppo",

            "iqoo",

            "nothing",

            "motorola",

            "google"

        ]

        for brand in brands:

            if brand in message_lower:

                result["brand"] = brand

                break


        # Detect Search Intent
        search_keywords = [

            "specification",

            "specs",

            "details",

            "tell me about"

        ]

        if any(
            keyword in message_lower
            for keyword
            in search_keywords
        ):

            result["intent"] = "search"

            result["phone_name"] = message


        return result