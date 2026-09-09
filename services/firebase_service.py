import os
import firebase_admin

from firebase_admin import (
    credentials,
    firestore,
    auth
)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SERVICE_ACCOUNT_PATH = os.path.join(
    BASE_DIR,
    "serviceAccountKey.json"
)


def initialize_firebase():

    if not firebase_admin._apps:

        cred = credentials.Certificate(
            SERVICE_ACCOUNT_PATH
        )

        firebase_admin.initialize_app(cred)

    return firestore.client()


db = initialize_firebase()


def verify_token(token):

    try:

        decoded_token = auth.verify_id_token(
            token
        )

        return decoded_token

    except Exception as error:

        print(
            "Token verification error:",
            error
        )

        return None


def save_chat(
    user_id,
    message,
    response
):

    db.collection(
        "chat_history"
    ).add({

        "user_id": user_id,

        "message": message,

        "response": response,

        "timestamp":
            firestore.SERVER_TIMESTAMP

    })


def get_chat_history(
    user_id,
    limit=10
):

    chats = (

        db.collection("chat_history")

        .where(
            "user_id",
            "==",
            user_id
        )

        .limit(limit)

        .stream()

    )

    history = []

    for chat in chats:

        data = chat.to_dict()

        history.append({

            "message":
                data.get("message"),

            "response":
                data.get("response")

        })

    return history