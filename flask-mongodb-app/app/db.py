from flask_pymongo import PyMongo


def init_mongo(app):
    # MONGO_URI is loaded from the environment (see config.py and .env.example)
    mongo = PyMongo(app)
    return mongo