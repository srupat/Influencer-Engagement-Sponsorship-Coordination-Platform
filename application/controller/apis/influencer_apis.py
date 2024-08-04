from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

# the marshall_with decorator encodes data to send back to the user as JSON, while the
# RequestParser is used to create new objects with the JSON received from the frontend.

output_fields = {
    "name": fields.String,
    "category": fields.String,
    "niche": fields.String,
    "followers": fields.Integer
}

create_influencer_parser = reqparse.RequestParser()
create_influencer_parser.add_argument('name')
create_influencer_parser.add_argument('category')
create_influencer_parser.add_argument('niche')
create_influencer_parser.add_argument('followers')


class InfluencerAPI(Resource):
    @marshal_with(output_fields)
    def get(self, influencer_id=None):
        if influencer_id:
            influencer = Influencer.query.get(influencer_id)
            return influencer
        influencers = Influencer.query.all()
        return influencers

    @marshal_with(output_fields)
    def post(self):
        args = create_influencer_parser.parse_args()
        influencer = Influencer(name=args['name'], category=args['category'], niche=args['niche'],
                                followers=args['followers'])
        db.session.add(influencer)
        db.session.commit()
        return influencer, 201

    @marshal_with(output_fields)
    def put(self, influencer_id):
        influencer = Influencer.query.get(influencer_id)
        args = create_influencer_parser.parse_args()
        influencer.name = args['name']
        influencer.category = args['category']
        influencer.niche = args['niche']
        influencer.followers = args['followers']
        db.session.commit()
        return influencer

    @marshal_with(output_fields)
    def delete(self, influencer_id):
        influencer = Influencer.query.get(influencer_id)
        db.session.delete(influencer)
        db.session.commit()
        return "", 200
