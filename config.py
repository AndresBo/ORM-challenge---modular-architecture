import os

# create a Class object Config and inherit from it to create different configurations
class Config(object):
    # Flask-SQLAlchemy configuration that if True tracks modifications of objects and emit signal
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # access to .env and get the value of SECRET_KEY,  variable name can be any but needs to match 
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")

    # creates getter and setter methods for the property
    @property
    # gets location of database URI
    def SQLALCHEMY_DATABASE_URI(self):
        # access .env and get the value of DATABASE_URL, the variable name can by any but needs to match
        value = os.environ.get("DATABASE_URL")
        # use ValueError to let user, there's something missing
        if not value:
            raise ValueError("DATABASE_URL is not set")
        
        return value


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


# get the configuration we are using from .flaskenv
environment = os.environ.get("FLASK_DEBUG")

# determine type of environment
if environment:
    app_config = DevelopmentConfig()
else:
    app_config = ProductionConfig()
