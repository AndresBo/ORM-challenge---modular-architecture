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
    # to create out database object and use ORM
    db.init_app(app)

    # import the controllers and activates the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    @app.get("/")
    def hello():
        return { "message": "HI Bob!"}

    return app
