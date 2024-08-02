from flask import Blueprint
from flask_security import login_required
from application.auth.auth import roles_required
from application.data.models import Sponsor

sponsor_bp = Blueprint('sponsor', __name__)


@sponsor_bp.route('/', methods=['GET', 'POST'])
# @login_required
@roles_required('sponsor')
def admin_home():
    return 'hello sponsor', 201


@sponsor_bp.route('/<string:name>', methods=['GET'])
def get_sponsor_by_username(name):
    sponsor = Sponsor.query.filter_by(name=name).first()
    if sponsor:
        return {'id': sponsor.id}, 200
    else:
        return {'error': 'Sponsor not found'}, 404