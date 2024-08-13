from flask import render_template, redirect, url_for, jsonify
from flask_security import login_required
from flask import Blueprint
from flask_security import logout_user
from sqlalchemy import func
from application.jobs import tasks
from datetime import datetime
from application.send_email import send_email


main_bp = Blueprint('main', __name__)

@main_bp.route("/hello", methods=["GET", "POST"])
def hello():
    now = datetime.now()
    print("now in flask =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time = ", dt_string)
    job = tasks.print_current_time_job.apply_async(countdown=10)
    result = job.wait()
    return str(result), 200

@main_bp.route('/influencers/request', methods=["GET", "POST"])
def query_influencers_with_pending_requests():
    from application.data.models import AdRequest, Influencer, User
    
    ad_requests = AdRequest.query.filter(AdRequest.is_pending == 1)
    influencers_ids = set()
    for request in ad_requests:
        influencers_ids.add(request.influencer_id)
    print(influencers_ids)
    influencer_emails = []
    for id in influencers_ids:
        print(id)
        influencer = Influencer.query.get(id)
        user = User.query.filter(User.username == influencer.name).first()
        influencer_emails.append(user.email)
    subject = 'Reminder: You have pending ad requests'
    body = 'Please check your account for pending ad requests.'
    for email in influencer_emails:
        send_email(subject, body, email)
    return jsonify(influencer_emails), 200

@main_bp.route('/export_csv/<int:sponsor_id>', methods=["POST"])
def export_campaigns(sponsor_id):
    job = tasks.export_campaigns_csv.apply_async(args=[sponsor_id])
    return jsonify({"task_id": job.id}), 200

@main_bp.route('/roles', methods=["GET"])
# @cache.cached(timeout=300)
def get_roles_users():
    from application.data.models import User, Role, roles_users
    from application.data.database import db
    num_admins = count_users_by_role('Admin')
    num_sponsors = count_users_by_role('Sponsor')
    num_influencers = count_users_by_role('Influencer')
    
    return jsonify({"Admins": num_admins, "Sponsors": num_sponsors, "Influencers": num_influencers}), 200

def count_users_by_role(role_name):
    from application.data.models import User, Role, roles_users
    from application.data.database import db
    return db.session.query(func.count(User.id)).join(roles_users).join(Role).filter(Role.name == role_name).scalar()
