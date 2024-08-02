from functools import wraps
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
    get_jwt, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
)
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from application.data.database import db
from application.data.models import *

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    auth_data = request.get_json()
    username = auth_data['username']
    password = auth_data['password']
    email = auth_data['email']
    role = auth_data['role']  
    
    if(role == 'Sponsor'):
        company_desc = auth_data['company_desc']
        industry = auth_data['industry']
        budget = auth_data['budget']
        
    if(role == "Influencer"):
        category = auth_data['category']
        niche = auth_data['niche']
        followers = auth_data['followers']

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        user.active = True

        role_from_db = Role.query.filter_by(name=role).first()
        if not role_from_db:
            return jsonify(message="Invalid role provided."), 400

        user.roles = [role_from_db]  
        
        if(role == 'Sponsor'):
            sponsor = Sponsor(name=username, company_desc=company_desc, industry=industry, budget=budget)
            db.session.add(sponsor)
            db.session.commit()
            
        if(role == 'Influencer'):
            influencer = Influencer(name=username, category=category, niche=niche, followers=followers)
            db.session.add(influencer)
            db.session.commit()

        db.session.add(user)
        db.session.commit()

        user_identity = {
            'id': user.id,
            'username': user.username,
            'role': role_from_db.name
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
            'role': user.roles[0].name  
        }
        access_token = create_access_token(identity=user_identity, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(identity=user_identity)

        response = jsonify({'role': user.roles[0].name})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        
        # Debug statements
        print("Access token set:", access_token)
        print("Refresh token set:", refresh_token)
        
        return response, 200
    else:
        return jsonify(message="Invalid credentials."), 401

@auth_bp.route('/logout', methods=['OPTIONS', 'POST'])
@jwt_required()
def logout():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight request'}), 200

    response = jsonify(message="Logout successful.")
    unset_jwt_cookies(response)
    return response, 200

def roles_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get('role', '')
            if user_role not in allowed_roles:
                return jsonify({'message': 'Access denied!'}), 403
            return f(*args, **kwargs)

        return wrapper

    return decorator

@auth_bp.route('/admin', methods=['GET'])
@roles_required(['admin'])
def admin():
    return jsonify({'message': 'Welcome, Admin!'})
