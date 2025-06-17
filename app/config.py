import os

class Config:
    """
    Configuration for the Flask app.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///superheroes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
