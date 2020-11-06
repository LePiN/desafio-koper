from flask import Flask
from api.extensions import database
from api.extensions import configurations
from api.resources import services


def create_app(**config):
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///teste.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # database.init_app(app)
    # services.init_app(app)
    configurations.init_app(app, **config)
    configurations.load_extensions(app)
    return app
