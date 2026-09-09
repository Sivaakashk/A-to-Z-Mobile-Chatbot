import json
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from services.firebase_service import db


def seed_database():

    with open(
        "data/sample_phones.json",
        "r",
        encoding="utf-8"
    ) as file:

        phones = json.load(file)


    for phone in phones:

        phone_id = (

            phone["full_name"]

            .lower()

            .replace(" ", "_")

        )

        db.collection(

            "phones"

        ).document(

            phone_id

        ).set(phone)


        print(
            f"Added: {phone['full_name']}"
        )


if __name__ == "__main__":

    seed_database()

    print(
        "Firebase database seeded successfully!"
    )