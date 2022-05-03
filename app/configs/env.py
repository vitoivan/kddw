from dotenv import load_dotenv
from os import environ
from flask import Flask

load_dotenv()

def init_app(app: Flask):
    
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')