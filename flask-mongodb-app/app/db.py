from flask_pymongo import PyMongo

def init_mongo(app):
    app.config["MONGO_URI"] = "mongodb+srv://admin:admin@clusterudla01.7uwannp.mongodb.net/catequesis_parroquial"
    mongo = PyMongo(app)
    return mongo