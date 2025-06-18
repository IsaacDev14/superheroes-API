# app/resources/hero.py
from flask_restful import Resource
from app.database import db
from app.models import Hero

class HeroList(Resource):
    """Handle GET requests for all heroes."""
    def get(self):
        heroes = Hero.query.all()
        return [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes], 200

class HeroDetail(Resource):
    """Handle GET requests for a single hero."""
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {'error': 'Hero not found'}, 404
        return hero.to_dict(rules=('hero_powers.power',)), 200