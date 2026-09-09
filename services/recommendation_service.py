from services.phone_service import PhoneService


class RecommendationService:

    @staticmethod
    def recommend(
        budget=None,
        brand=None,
        purpose=None
    ):

        phones = PhoneService.get_all_phones()

        filtered_phones = []

        for phone in phones:

            # Budget Filter
            if budget:

                if phone.get(
                    "price",
                    999999
                ) > budget:

                    continue

            # Brand Filter
            if brand:

                if phone.get(
                    "brand",
                    ""
                ).lower() != brand.lower():

                    continue

            filtered_phones.append(phone)

        # Ranking
        ranked_phones = []

        for phone in filtered_phones:

            score = 0

            ratings = phone.get(
                "ratings",
                {}
            )

            if purpose == "gaming":

                score += ratings.get(
                    "gaming",
                    0
                )

            elif purpose == "camera":

                score += ratings.get(
                    "camera",
                    0
                )

            elif purpose == "battery":

                score += ratings.get(
                    "battery",
                    0
                )

            elif purpose == "display":

                score += ratings.get(
                    "display",
                    0
                )

            else:

                score += (
                    ratings.get(
                        "overall",
                        0
                    )
                )

            phone["recommendation_score"] = score

            ranked_phones.append(phone)

        ranked_phones.sort(

            key=lambda x:
                x.get(
                    "recommendation_score",
                    0
                ),

            reverse=True

        )

        return ranked_phones[:5]