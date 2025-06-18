from flask_restful import Resource, reqparse
from flask import jsonify
from ..models import HeroPower, Hero, Power
from ..extensions import db

class HeroPowerResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('strength', type=str, required=True, choices=('Strong', 'Weak', 'Average'), help="Strength must be Strong, Weak, or Average")
        parser.add_argument('power_id', type=int, required=True, help="power_id is required")
        parser.add_argument('hero_id', type=int, required=True, help="hero_id is required")
        args = parser.parse_args()

        hero = Hero.query.get(args['hero_id'])
        power = Power.query.get(args['power_id'])

        if not hero:
            return {"errors": ["Hero not found"]}, 404
        if not power:
            return {"errors": ["Power not found"]}, 404

        try:
            hero_power = HeroPower(strength=args['strength'], hero=hero, power=power)
            db.session.add(hero_power)
            db.session.commit()
            result = hero_power.to_dict()
            # Add nested hero and power details
            result['hero'] = hero.to_dict(only=['id', 'name', 'super_name'])
            result['power'] = power.to_dict(only=['id', 'name', 'description'])
            return jsonify(result)
        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400
