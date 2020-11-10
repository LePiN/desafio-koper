from flask import Flask
from api.extensions import configurations


def create_app(**config):
    app = Flask(__name__)
    configurations.init_app(app, **config)
    configurations.load_extensions(app)
    return app
