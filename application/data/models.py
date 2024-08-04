from .database import db
from flask_security import UserMixin, RoleMixin
# from flask_sqlalchemy import ForeignKey
import datetime

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    username = db.Column(db.String(255), unique=True)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Sponsor(db.Model):
    __tablename__ = 'sponsor'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    company_desc = db.Column(db.String(255))
    industry = db.Column(db.String(80))
    budget = db.Column(db.BigInteger)


class Influencer(db.Model):
    __tablename__ = 'influencer'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(100))
    niche = db.Column(db.String(80))
    followers = db.Column(db.Integer())


class AdRequest(db.Model):
    __tablename__ = 'ad_request'
    id = db.Column(db.Integer(), primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"))
    influencer_id = db.Column(db.Integer, db.ForeignKey("influencer.id"))
    description = db.Column(db.String(255))
    requirements = db.Column(db.String(255), nullable=False)
    payment_amount = db.Column(db.Integer(), nullable=False)
    is_pending = db.Column(db.Integer, nullable=False, default=0)
    is_accepted = db.Column(db.Integer, nullable=False, default=0)


class Campaign(db.Model):
    __tablename__ = 'campaign'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False)
    budget = db.Column(db.BigInteger)
    is_public = db.Column(db.Integer, nullable=False, default=0)
    is_flagged = db.Column(db.Integer, nullable=False, default=0)
    sponsor_id = db.Column(db.Integer, db.ForeignKey("sponsor.id"))
    
    
class CampaignGoal(db.Model):
    __tablename__ = 'campaign_goals'
    id = db.Column(db.Integer(), primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"))
    goal = db.Column(db.String(255), nullable=False)
    

