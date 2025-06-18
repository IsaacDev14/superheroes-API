from flask import Flask
from .extensions import db, migrate, api
from .resources.hero import HeroListResource, HeroResource
from .resources.power import PowerListResource, PowerResource
from .resources.hero_power import HeroPowerResource
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Register resources and endpoints
    api.add_resource(HeroListResource, '/heroes')
    api.add_resource(HeroResource, '/heroes/<int:hero_id>')
    api.add_resource(PowerListResource, '/powers')
    api.add_resource(PowerResource, '/powers/<int:power_id>')
    api.add_resource(HeroPowerResource, '/hero_powers')

    return app
