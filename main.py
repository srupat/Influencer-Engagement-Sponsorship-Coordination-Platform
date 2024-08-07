import os
from flask import Flask
from flask.scaffold import setupmethod
from flask_migrate import Migrate
from application.auth.auth import auth_bp
from application.controller.admin.controllers import admin_bp
from application.controller.apis.ad_request_apis import AdRequestAPI
from application.controller.influencer.controllers import influencer_bp
from application.controller.sponsor.controllers import sponsor_bp
from application.controller.campaign.controllers import campaign_bp
from application.controller.ad_request.controllers import request_bp
from application.controller.controllers import main
from application.utils.config import LocalDevelopmentConfig
from flask_restful import Api
from application.data.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.data.models import *
from application.controller.apis.influencer_apis import InfluencerAPI
from application.controller.apis.sponsor_apis import SponsorAPI
from application.controller.apis.campaign_apis import CampaignAPI
from application.controller.apis.user_apis import UserAPI
from application.controller.apis.campaign_goals_apis import CampaignGoalAPI
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import timedelta
from application.jobs.workers import make_celery

def register_routes(app):
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(influencer_bp, url_prefix='/influencer')
    app.register_blueprint(sponsor_bp, url_prefix='/sponsor')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(campaign_bp, url_prefix='/campaign')
    app.register_blueprint(request_bp, url_prefix='/request')
    app.register_blueprint(main)

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    register_routes(app)
    cors = CORS(app, supports_credentials=True)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)
    
    celery = make_celery(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['id']

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        return {'roles': identity['role']}

    with app.app_context():
        db.create_all()
        
    app.app_context().push()

    return app, api, celery

app, api, celery = create_app()

api.add_resource(InfluencerAPI, '/api/influencer', '/api/influencer/<int:influencer_id>')
api.add_resource(SponsorAPI, '/api/sponsor', '/api/sponsor/<int:sponsor_id>')
api.add_resource(AdRequestAPI, '/api/ad_request', '/api/ad_request/<int:ad_request_id>', '/api/campaign/request/<int:campaign_id>', '/api/influencer/request/<int:influencer_id>', '/api/ad_request/<string:action>/<int:ad_request_id>', '/api/ad_request/<string:action>/<int:ad_request_id>')
api.add_resource(CampaignAPI, '/api/campaign', '/api/campaign/<int:campaign_id>', '/api/campaign/sponsor/<int:sponsor_id>', '/api/campaign/influencer/<int:influencer_id>')
api.add_resource(UserAPI, '/api/user', '/api/user/<int:user_id>')
api.add_resource(CampaignGoalAPI, '/api/goal', '/api/goal/<int:campaign_id>')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8085)
