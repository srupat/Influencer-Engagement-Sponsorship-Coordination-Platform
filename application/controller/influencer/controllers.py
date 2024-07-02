from flask import Blueprint
from flask_security import login_required, roles_required

influencer_bp = Blueprint('influencer', __name__)


@influencer_bp.route('/', methods=['GET', 'POST'])
@login_required
@roles_required('influencer')
def admin_home():
    return 'hello influencer'
