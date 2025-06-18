# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_restful import Api

# Initialize extensions
db = SQLAlchemy()
alembic = Alembic()
api = Api()

def create_app():
    """Application factory to initialize Flask app."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    alembic.init_app(app)
    api.init_app(app)
    
    # Register blueprints or resources
    from app.resources import initialize_resources
    initialize_resources(api)
    
    return app