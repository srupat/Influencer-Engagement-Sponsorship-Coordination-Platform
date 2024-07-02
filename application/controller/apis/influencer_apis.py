from flask_restful import Resource, fields, marshal_with, reqparse
from application.data.database import db
from application.data.models import *
from application.utils.validation import *

# the marshall_with decorator encodes data to send back to the user as JSON, while the
# RequestParser is used to create new objects with the JSON received from the frontend.


