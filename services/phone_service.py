from services.firebase_service import db


class PhoneService:

    @staticmethod
    def get_all_phones():

        phones = (
            db.collection("phones")
            .stream()
        )

        results = []

        for phone in phones:

            data = phone.to_dict()

            data["id"] = phone.id

            results.append(data)

        return results


    @staticmethod
    def get_phone_by_id(phone_id):

        phone = (
            db.collection("phones")
            .document(phone_id)
            .get()
        )

        if phone.exists:

            data = phone.to_dict()

            data["id"] = phone.id

            return data

        return None


    @staticmethod
    def search_by_brand(brand):

        if brand is None:
            return []

        brand = str(brand).strip()

        if not brand:
            return []

        phones = (

            db.collection("phones")

            .where(
                "brand",
                "==",
                brand
            )

            .stream()

        )

        return [

            {
                "id": phone.id,
                **phone.to_dict()
            }

            for phone in phones

        ]


    @staticmethod
    def search_by_budget(max_price):

        try:
            max_price = float(max_price)
        except (TypeError, ValueError):
            return []

        phones = (

            db.collection("phones")

            .where(
                "price",
                "<=",
                max_price
            )

            .order_by("price")

            .limit(20)

            .stream()

        )

        return [

            {
                "id": phone.id,
                **phone.to_dict()
            }

            for phone in phones

        ]


    @staticmethod
    def search_by_name(query):

        if query is None:
            return []

        query = str(query).strip().lower()

        if not query:
            return []

        all_phones = PhoneService.get_all_phones()

        results = []

        for phone in all_phones:

            full_name = str(phone.get("full_name", "")).lower()

            brand = str(phone.get("brand", "")).lower()

            model = str(phone.get("model", "")).lower()

            if (
                query in full_name
                or query in brand
                or query in model
            ):

                results.append(phone)

        return results