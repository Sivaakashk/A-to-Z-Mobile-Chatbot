from flask import Flask
from flask_cors import CORS

from config import Config

from routes.chat_routes import chat_bp
from routes.phone_routes import phone_bp
from routes.auth_routes import auth_bp


def create_app():

    app = Flask(
        __name__,
        template_folder="template"
    )

    app.config.from_object(Config)

    CORS(app)

    # Register Blueprints
    app.register_blueprint(chat_bp)
    app.register_blueprint(phone_bp)
    app.register_blueprint(auth_bp)

    return app


app = create_app()
import flask


@app.route("/")
def home():
    return flask.render_template("index.htm")


if __name__ == "__main__":

    import os

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )