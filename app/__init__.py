from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    from .config import Config
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)  # Initialize API with the app

    # Import models after db initialization to avoid circular imports
    from .models import Hero, Power, HeroPower

    # Import and register routes
    from .routes.hero import HeroListResource, HeroDetailResource
    from .routes.power import PowerListResource, PowerDetailResource, PowerUpdateResource
    from .routes.hero_power import HeroPowerCreateResource

    # Register API resources
    api.add_resource(HeroListResource, '/heroes')
    api.add_resource(HeroDetailResource, '/heroes/<int:id>')
    api.add_resource(PowerListResource, '/powers')
    api.add_resource(PowerDetailResource, '/powers/<int:id>')
    api.add_resource(PowerUpdateResource, '/powers/<int:id>')
    api.add_resource(HeroPowerCreateResource, '/hero_powers')

    # Print registered routes for debugging
    with app.app_context():
        print("🔗 Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.rule} -> {rule.endpoint}")

    return app