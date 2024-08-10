from flask import Blueprint
from application.data.models import Campaign, CampaignGoal
from application.data.database import db

campaign_bp = Blueprint('campaign', __name__)

@campaign_bp.route('/public/<int:campaign_id>', methods=['PUT'])
def make_campaign_public(campaign_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    campaign.is_public = 1
    db.session.commit()
    return 'Campaign made public', 200

@campaign_bp.route('/progress/<int:campaign_id>', methods=['GET'])
def get_progress(campaign_id):
    goals = CampaignGoal.query.filter_by(campaign_id=campaign_id).all()
    completed_goals = CampaignGoal.query.filter_by(campaign_id=campaign_id, is_completed=1).all()
    progress = len(completed_goals) / len(goals) * 100
    return {'progress': int(progress)}, 200
    
    
@campaign_bp.route('/complete/<int:goal_id>', methods=['PUT'])
def complete_ad_request(goal_id):
    goal = CampaignGoal.query.filter_by(id=goal_id).first()
    goal.is_completed = 1
    db.session.commit()
    return 'goal completed', 200