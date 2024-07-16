from flask import render_template, redirect, url_for
from flask_security import login_required
from flask import Blueprint
from flask_security import logout_user

from application.auth.auth import roles_required

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template("home.html")


# @main.route('/logout', methods=['GET'])
# def logout():
#     logout_user()
#     return redirect(url_for('main.home'))


# @main.route('/login', methods=['GET', 'POST'])
# def custom_login():
#     form = ExtendedLoginForm(request.form)
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and verify_and_update_password(form.password.data, user):
#             login_user(user, remember=form.remember.data)
#             if form.admin.data:
#                 return redirect(url_for('main.admin'))
#             elif form.sponsor.data:
#                 return redirect(url_for('main.sponsor'))
#             elif form.influencer.data:
#                 return redirect(url_for('main.influencer'))
#             return redirect(url_for('main.home'))
#     return render_template('security/login_user.html', form=form)
#
#
@main.route('/admin')
@roles_required('admin')
def admin():
    return "Admin Page"


@main.route('/sponsor')
@roles_required('sponsor')
def sponsor():
    return "Sponsor Page"


@main.route('/influencer')
@roles_required('influencer')
def influencer():
    return "Influencer Page"
