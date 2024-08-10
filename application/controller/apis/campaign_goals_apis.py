from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

output_fields = {
    "id": fields.Integer,
    "campaign_id": fields.Integer,
    "goal": fields.String,
    "is_completed": fields.Integer
}

create_goal_parser = reqparse.RequestParser()
create_goal_parser.add_argument('campaign_id')
create_goal_parser.add_argument('goal')

class CampaignGoalAPI(Resource):
    @marshal_with(output_fields)
    def get(self, campaign_id=None):
        if campaign_id:
            campaign_goals = CampaignGoal.query.filter(CampaignGoal.campaign_id == campaign_id).all()
            return campaign_goals
        campaign_goals = CampaignGoal.query.all()
        return campaign_goals

    @marshal_with(output_fields)
    def post(self):
        args = create_goal_parser.parse_args()
        campaign_goal = CampaignGoal(
            campaign_id=args['campaign_id'],
            goal=args['goal']
        )
        db.session.add(campaign_goal)
        db.session.commit()
        return campaign_goal

    @marshal_with(output_fields)
    def put(self, goal_id):
        campaign_goal = CampaignGoal.query.get(goal_id)
        args = create_goal_parser.parse_args()
        campaign_goal.campaign_id = args['campaign_id']
        campaign_goal.goal = args['goal']
        db.session.commit()
        return campaign_goal

    def delete(self, goal_id):
        campaign_goal = CampaignGoal.query.get(goal_id)
        db.session.delete(campaign_goal)
        db.session.commit()
        return {'message': 'Campaign goal deleted successfully'}, 204