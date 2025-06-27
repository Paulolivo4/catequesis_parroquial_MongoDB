from flask import Flask
from .db import init_mongo
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'Softw@re2025'  # Necesario para flash
    app.mongo = init_mongo(app)  # Inicializa la conexión a MongoDB

    app.register_blueprint(bp)   # Registra las rutas

    return app