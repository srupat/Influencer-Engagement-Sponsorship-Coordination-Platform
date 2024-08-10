from application.auth.auth import roles_required
from application.data.models import AdRequest
from application.data.database import db
from flask import Blueprint

request_bp = Blueprint('request', __name__)

@request_bp.route('/<int:ad_request_id>/<int:influencer_id>', methods=['PUT'])
def request_ad_request_influencer(ad_request_id, influencer_id):
    ad_request = AdRequest.query.get(ad_request_id)
    ad_request.influencer_id = influencer_id
    db.session.commit()
    return 'influencer assigned', 201

@request_bp.route('/accept/<int:ad_request_id>/', methods=['PUT'])
def allot_ad_request(ad_request_id):
    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return 'Ad request not found', 404
    ad_request.is_pending = 0
    db.session.commit()
    return 'Ad request allotted', 200


@request_bp.route('/reject/<int:ad_request_id>', methods=['PUT'])
def reject_influencer_request(ad_request_id):
    ad_request = AdRequest.query.get(ad_request_id)
    ad_request.influencer_id = None
    db.session.commit()
    return 'influencer request rejected', 201

@request_bp.route('/complete/<int:ad_request_id>', methods=['PUT'])
def complete_ad_request(ad_request_id):
    ad_request = AdRequest.query.get(ad_request_id)
    ad_request.is_completed = 1
    db.session.commit()
    return 'Ad request completed', 200