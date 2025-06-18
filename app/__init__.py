from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Import and register resources
    from .routes.hero import HeroListResource, HeroDetailResource
    from .routes.power import PowerListResource, PowerDetailResource, PowerUpdateResource
    from .routes.hero_power import HeroPowerCreateResource

    # Register routes with the API
    api.add_resource(HeroListResource, '/heroes')
    api.add_resource(HeroDetailResource, '/heroes/<int:id>')
    api.add_resource(PowerListResource, '/powers')
    api.add_resource(PowerDetailResource, '/powers/<int:id>')
    api.add_resource(PowerUpdateResource, '/powers/<int:id>')
    api.add_resource(HeroPowerCreateResource, '/hero_powers')

    return app
