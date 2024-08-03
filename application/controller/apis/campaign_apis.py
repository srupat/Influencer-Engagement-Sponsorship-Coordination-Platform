from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *
from datetime import datetime

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
    def get(self, campaign_id=None, sponsor_id=None, influencer_id=None):      
        if campaign_id:
            campaign = Campaign.query.get(campaign_id)
            print("campaign id")
            return campaign
        if sponsor_id:
            campaigns = Campaign.query.filter(Campaign.sponsor_id == sponsor_id).all()
            print("sponsor id")
            return campaigns
        if influencer_id:
            campaigns = Campaign.query.filter(Campaign.influencer_id == influencer_id).all()
            print("influencer id")
            return campaigns
        campaigns = Campaign.query.all()
        print("all")
        return campaigns
        
    
    @marshal_with(output_fields)
    def put(self, campaign_id):
        campaign = Campaign.query.get(campaign_id)
        args = campaign_parser.parse_args()
        campaign.name = args['name']
        
        try:
            campaign.start_date = datetime.strptime(args['start_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            campaign.end_date = datetime.strptime(args['end_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError as e:
            return {'message': f'Invalid date format: {e}'}, 400
        
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