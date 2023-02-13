from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 
def create_app():
    # create the flask app abject 
    app = Flask(__name__)

    # got app.config object. from object load app_config
    app.config.from_object("config.app_config")

    # associates create_app with db object created outside
    # to create out database object
    db.init_app(app)

    @app.get("/")
    def hello():
        return { "message": "HI Bob!"}

    return app
