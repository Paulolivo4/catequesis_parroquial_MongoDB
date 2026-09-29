import os


class Config:
    # Set SECRET_KEY in your environment for any real deployment.
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24).hex()
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/catequesis_parroquial'