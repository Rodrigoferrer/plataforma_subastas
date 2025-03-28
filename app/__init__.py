from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
# from flask_jwt_extended import JWTManager
# from flask_bcrypt import Bcrypt


# bcrypt = Bcrypt()
# jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    # bcrypt.init_app(app)
    # jwt.init_app(app)
    
    api = Api(app, version='1.0', title='Subasta API TEST', description='Subasta Application API TEST')

    from app.api.users import api as users_ns

    api.add_namespace(users_ns, path='/api/v1/users')
    # api.add_namespace(amenities_ns, path='/api/v1/amenities')
    # api.add_namespace(places_ns, path='/api/v1/places')
    # api.add_namespace(reviews_ns, path='/api/v1')
    # api.add_namespace(auth_ns, path='/api/v1/auth')

    return app