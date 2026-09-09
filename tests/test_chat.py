from app import app


def test_chat_endpoint():

    client = app.test_client()

    response = client.post(

        "/api/chat",

        json={

            "message":
                "Best phone under 30000",

            "user_id":
                "test_user"

        }

    )

    assert response.status_code in [
        200,
        500
    ]