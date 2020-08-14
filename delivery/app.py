from flask import Flask

from delivery.ext import config
from delivery.ext import db
from delivery.ext import cli


def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)

    return app
