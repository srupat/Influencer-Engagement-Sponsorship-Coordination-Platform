from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

output_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "start_date": fields.DateTime,
    "end_date": fields.DateTime,
    "budget": fields.Integer,
    "is_public": fields.Integer,
    "is_flagged": fields.Integer
}

campaign_parser = reqparse.RequestParser()
campaign_parser.add_argument('name')
campaign_parser.add_argument('start_date')
campaign_parser.add_argument('end_date')
campaign_parser.add_argument('budget')

class CampaignAPI(Resource):
    @marshal_with(output_fields)
    def get(self, campaign_id=None):
        if campaign_id is None:
            campaigns = Campaign.query.all()
            return campaigns
        campaign = Campaign.query.get(campaign_id)
        return campaign

    @marshal_with(output_fields)
    def put(self, campaign_id):
        campaign = Campaign.query.get(campaign_id)
        args = campaign_parser.parse_args()
        campaign.name = args['name']
        campaign.start_date = args['start_date']
        campaign.end_date = args['end_date']
        campaign.budget = args['budget']
        db.session.commit()
        return campaign

    @marshal_with(output_fields)
    def delete(self, campaign_id):
        campaign = Campaign.query.get(campaign_id)
        db.session.delete(campaign)
        db.session.commit()
        return "", 200

    @marshal_with(output_fields)
    def post(self):
        args = campaign_parser.parse_args()
        campaign = Campaign(name=args['name'], start_date=args['start_date'], end_date=args['end_date'], budget=args['budget'])
        db.session.add(campaign)
        db.session.commit()
        return campaign, 201