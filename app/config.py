# app/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///superheroes.db'  # Local DB file
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Turn off unnecessary warnings
