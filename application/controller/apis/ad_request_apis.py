from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

output_fields = {
    "description": fields.String,
    "requirements": fields.String,
    "payment_amount": fields.Integer
}

update_ad_request_parser = reqparse.RequestParser()
update_ad_request_parser.add_argument('description')
update_ad_request_parser.add_argument('requirements')
update_ad_request_parser.add_argument('payment_amount')

create_ad_request_parser = reqparse.RequestParser()
create_ad_request_parser.add_argument('description')
create_ad_request_parser.add_argument('requirements')
create_ad_request_parser.add_argument('payment_amount')

class AdRequestAPI(Resource):
    @marshal_with(output_fields)
    def get(self, ad_request_id):
        ad_request = AdRequest.query.get(ad_request_id)
        return ad_request

    @marshal_with(output_fields)
    def put(self, ad_request_id):
        ad_request = AdRequest.query.get(ad_request_id)
        args = update_ad_request_parser.parse_args()
        ad_request.description = args['description']
        ad_request.requirements = args['requirements']
        ad_request.payment_amount = args['payment_amount']
        db.session.commit()
        return ad_request

    @marshal_with(output_fields)
    def delete(self, ad_request_id):
        ad_request = AdRequest.query.get(ad_request_id)
        db.session.delete(ad_request)
        db.session.commit()
        return "", 200

    @marshal_with(output_fields)
    def post(self):
        args = create_ad_request_parser.parse_args()
        ad_request = AdRequest(description=args['description'], requirements=args['requirements'], payment_amount=args['payment_amount'])
        db.session.add(ad_request)
        db.session.commit()
        return ad_request, 201