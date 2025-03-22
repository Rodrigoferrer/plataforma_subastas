from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.user import Usuario


api = Namespace('users', description='User operations')
