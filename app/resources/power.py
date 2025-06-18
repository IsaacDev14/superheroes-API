# app/resources/power.py
from flask_restful import Resource, reqparse
from app.database import db
from app.models import Power

class PowerList(Resource):
    """Handle GET requests for all powers."""
    def get(self):
        powers = Power.query.all()
        return [power.to_dict(only=('id', 'name', 'description')) for power in powers], 200

class PowerDetail(Resource):
    """Handle GET and PATCH requests for a single power."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', type=str, required=True, help='Description is required')
    
    def get(self, id):
        power = Power.query.get(id)
        if not power:
            return {'error': 'Power not found'}, 404
        return power.to_dict(only=('id', 'name', 'description')), 200
    
    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return {'error': 'Power not found'}, 404
        
        args = self.parser.parse_args()
        try:
            power.description = args['description']
            db.session.commit()
            return power.to_dict(only=('id', 'name', 'description')), 200
        except ValueError as e:
            return {'errors': [str(e)]}, 400