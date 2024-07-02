import os
from flask import Flask
from flask.scaffold import setupmethod
from application.controller.admin.controllers import admin_bp
from application.controller.influencer.controllers import influencer_bp
from application.controller.sponsor.controllers import sponsor_bp
from application.utils.config import LocalDevelopmentConfig
from flask_restful import Api
from application.controller.controllers import *
from application.data.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.data.models import *


def register_routes(app):
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(influencer_bp, url_prefix='/influencer')
    app.register_blueprint(sponsor_bp, url_prefix='/sponsor')
    app.register_blueprint(main)


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    register_routes(app)

    with app.app_context():
        db.create_all()

    return app, api


app, api = create_app()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8085)
