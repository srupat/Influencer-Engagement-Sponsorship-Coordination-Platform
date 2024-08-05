from flask import Blueprint
from flask_security import login_required, roles_required
from application.auth.auth import roles_required
from application.data.models import Influencer

influencer_bp = Blueprint('influencer', __name__)


@influencer_bp.route('/', methods=['GET', 'POST'])
# @login_required
@roles_required('influencer')
def admin_home():
    return 'hello influencer', 201


@influencer_bp.route('/<string:name>', methods=['GET'])
def get_sponsor_by_username(name):
    influencer = Influencer.query.filter_by(name=name).first()
    if influencer:
        return {'id': influencer.id}, 200
    else:
        return {'error': 'Influencer not found'}, 404