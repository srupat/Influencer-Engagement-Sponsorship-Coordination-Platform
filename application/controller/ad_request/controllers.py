from application.auth.auth import roles_required
from application.data.models import AdRequest

@roles_required('Admin')
@app.route('/ad_request/<int:campaign_id>', methods=['GET'])
def get_ad_request_by_campaign_id(campaign_id):
    ad_requests = AdRequest.query.filter_by(campaign_id=campaign_id).all()
    return ad_requests, 200