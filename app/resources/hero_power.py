# app/resources/hero_power.py
from flask_restful import Resource, reqparse
from app.database import db
from app.models import HeroPower, Hero, Power

class HeroPowerCreate(Resource):
    """Handle POST requests to create a new HeroPower."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('strength', type=str, required=True, help='Strength is required')
        self.parser.add_argument('hero_id', type=int, required=True, help='Hero ID is required')
        self.parser.add_argument('power_id', type=int, required=True, help='Power ID is required')
    
    def post(self):
        args = self.parser.parse_args()
        
        # Verify Hero and Power exist
        hero = Hero.query.get(args['hero_id'])
        power = Power.query.get(args['power_id'])
        
        if not hero or not power:
            return {'errors': ['Hero or Power not found']}, 404
        
        # Create new HeroPower
        hero_power = HeroPower(
            strength=args['strength'],
            hero_id=args['hero_id'],
            power_id=args['power_id']
        )
        
        try:
            db.session.add(hero_power)
            db.session.commit()
            return hero_power.to_dict(rules=('hero', 'power')), 201
        except ValueError as e:
            db.session.rollback()
            return {'errors': [str(e)]}, 400