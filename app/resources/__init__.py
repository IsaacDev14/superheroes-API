# app/resources/__init__.py
from flask_restful import Api
from .hero import HeroList, HeroDetail
from .power import PowerList, PowerDetail
from .hero_power import HeroPowerCreate

def initialize_resources(api: Api):
    """Register API resources with the Flask-RESTful Api instance."""
    api.add_resource(HeroList, '/heroes')
    api.add_resource(HeroDetail, '/heroes/<int:id>')
    api.add_resource(PowerList, '/powers')
    api.add_resource(PowerDetail, '/powers/<int:id>')
    api.add_resource(HeroPowerCreate, '/hero_powers')