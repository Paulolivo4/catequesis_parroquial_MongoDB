from flask import Flask
from .db import init_mongo
from .routes import bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # SECRET_KEY and MONGO_URI come from the environment
    app.mongo = init_mongo(app)  # Initializes the MongoDB connection

    app.register_blueprint(bp)  # Registers the routes

    return app