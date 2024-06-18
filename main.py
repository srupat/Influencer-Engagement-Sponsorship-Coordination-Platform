import os
from flask import Flask
from flask.scaffold import setupmethod

from application.utils.config import LocalDevelopmentConfig
from flask_restful import Api
from application.data.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.data.models import *


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    app.app_context().push()
    return app, api


app, api = create_app()


@setupmethod
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
    app.debug = True
