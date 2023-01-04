from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies import movies_ns
from app.views.directors import directors_ns
from app.views.genres import genres_ns


def create_app(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    create_data(application, db)


def create_data(application: Flask, data_base):
    with application.app_context():
        data_base.create_all()


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
