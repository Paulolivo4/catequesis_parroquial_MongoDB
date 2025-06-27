from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

class User(mongo.Document):
    username = mongo.StringField(required=True, unique=True)
    email = mongo.StringField(required=True, unique=True)
    password = mongo.StringField(required=True)

class Post(mongo.Document):
    title = mongo.StringField(required=True)
    content = mongo.StringField(required=True)
    author = mongo.ReferenceField(User)