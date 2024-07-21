from flask import Blueprint
from flask_security import login_required
from application.auth.auth import roles_required

sponsor_bp = Blueprint('sponsor', __name__)


@sponsor_bp.route('/', methods=['GET', 'POST'])
# @login_required
@roles_required('sponsor')
def admin_home():
    return 'hello sponsor', 201
