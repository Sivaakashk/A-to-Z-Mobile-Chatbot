import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")

    FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL")

    FIREBASE_PRIVATE_KEY = os.getenv(
        "FIREBASE_PRIVATE_KEY"
    )