# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration for the Flask application."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///superheroes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('FLASK_ENV') == 'development'