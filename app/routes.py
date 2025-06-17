# app/routes.py

from flask import Blueprint, jsonify

# Create a Blueprint instance for API routes
api = Blueprint('api', __name__)

@api.route('/')
def home():
    """
    Basic test route to verify that the API is working.
    """
    return jsonify({"message": "Welcome to the Superheroes API!"})
