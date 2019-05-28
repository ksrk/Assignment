import sys
from flask import Flask
from trails.stores import views


def create_app():
    check_version()
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(views.blueprint, url_prefix='/stores')


def check_version():
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")
