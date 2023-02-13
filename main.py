from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 
def create_app():
    #create the flask app abject 
    app = Flask(__name__)

    #configuring our app
    app.config.from_object("config.app_config")

    # creating our db object
    bd = SQLAlchemy(app)

    return app
