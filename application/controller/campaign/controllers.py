from flask import Blueprint
from application.data.models import Campaign
from application.data.database import db

campaign_bp = Blueprint('campaign', __name__)

@campaign_bp.route('/public/<int:campaign_id>', methods=['PUT'])
def make_campaign_public(campaign_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    campaign.is_public = 1
    db.session.commit()
    return 'Campaign made public', 200