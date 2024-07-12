from functools import wraps
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
    get_jwt, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
)
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from application.data.database import db
from application.data.models import User, Role

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    auth_data = request.get_json()
    username = auth_data['username']
    password = auth_data['password']
    email = auth_data['email']
    roles = auth_data['roles']

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        user.active = True
        user.roles = Role.query.filter(Role.name.in_(roles)).all()

        db.session.add(user)
        db.session.commit()

        user_identity = {
            'id': user.id,
            'username': user.username,
            'roles': [role.name for role in user.roles]
        }
        access_token = create_access_token(identity=user_identity)
        refresh_token = create_refresh_token(identity=user_identity)

        response = jsonify(message="User registered successfully.")
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response, 201
    else:
        return jsonify(message="User already exists."), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    username = auth_data['username']
    password = auth_data['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        user.active = True
        db.session.commit()

        user_identity = {
            'id': user.id,
            'username': user.username,
            'roles': [role.name for role in user.roles]
        }
        access_token = create_access_token(identity=user_identity, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(identity=user_identity)

        response = jsonify({'login': True})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    else:
        return jsonify(message="Invalid credentials."), 401


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify(message="Logout successful.")
    unset_jwt_cookies(response)
    return response, 200


def roles_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_roles = claims.get('roles', [])
            if not set(allowed_roles).intersection(set(user_roles)):
                return jsonify({'message': 'Access denied!'}), 403
            return f(*args, **kwargs)

        return wrapper

    return decorator


@auth_bp.route('/admin', methods=['GET'])
@roles_required(['admin'])
def admin():
    return jsonify({'message': 'Welcome, Admin!'})
