from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

output_fields = {
    "sponsor_id": fields.Integer,
    "name": fields.String,
    "company_desc": fields.String,
    "industry": fields.String,
    "budget": fields.Integer
}

create_sponsor_parser = reqparse.RequestParser()
create_sponsor_parser.add_argument('name')
create_sponsor_parser.add_argument('company_desc')
create_sponsor_parser.add_argument('industry')
create_sponsor_parser.add_argument('budget')

class SponsorAPI(Resource):
    @marshal_with(output_fields)
    def get(self, sponsor_id=None):
        if sponsor_id is None:
            sponsors = Sponsor.query.all()
            return sponsors
        sponsor = Sponsor.query.get(sponsor_id)
        return sponsor

    @marshal_with(output_fields)
    def post(self):
        args = create_sponsor_parser.parse_args()
        sponsor = Sponsor(name=args['name'], company_desc=args['company_desc'], industry=args['industry'],
                          budget=args['budget'])
        db.session.add(sponsor)
        db.session.commit()
        return sponsor, 201

    @marshal_with(output_fields)
    def put(self, sponsor_id):
        sponsor = Sponsor.query.get(sponsor_id)
        args = create_sponsor_parser.parse_args()
        sponsor.name = args['name']
        sponsor.company_desc = args['company_desc']
        sponsor.industry = args['industry']
        sponsor.budget = args['budget']
        db.session.commit()
        return sponsor

    @marshal_with(output_fields)
    def delete(self, sponsor_id):
        sponsor = Sponsor.query.get(sponsor_id)
        db.session.delete(sponsor)
        db.session.commit()
        return "", 200