from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register resources
    from .resources.hero_resource import HeroResource, HeroListResource
    from .resources.power_resource import PowerResource, PowerListResource

    api = Api(app)
    api.add_resource(HeroListResource, "/heroes")
    api.add_resource(HeroResource, "/heroes/<int:id>")
    api.add_resource(PowerListResource, "/powers")
    api.add_resource(PowerResource, "/powers/<int:id>")

    return app
