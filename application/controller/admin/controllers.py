from flask import Blueprint
from flask_security import login_required

from application.auth.auth import roles_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/', methods=['GET', 'POST'])
# @login_required
@roles_required('admin')
def admin_home():
    return 'hello admin', 201
