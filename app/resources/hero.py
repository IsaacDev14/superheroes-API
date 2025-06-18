from flask_restful import Resource, reqparse
from flask import jsonify
from ..models import Hero
from ..extensions import db

class HeroListResource(Resource):
    def get(self):
        # Return all heroes with id, name, super_name only
        heroes = Hero.query.all()
        return jsonify([hero.to_dict(only=['id', 'name', 'super_name']) for hero in heroes])

class HeroResource(Resource):
    def get(self, hero_id):
        hero = Hero.query.get(hero_id)
        if not hero:
            return {"error": "Hero not found"}, 404

        # Include hero_powers with nested power details, limit recursion
        hero_data = hero.to_dict()
        return jsonify(hero_data)
