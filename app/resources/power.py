from flask_restful import Resource, reqparse
from flask import jsonify, request
from ..models import Power
from ..extensions import db

class PowerListResource(Resource):
    def get(self):
        powers = Power.query.all()
        return jsonify([power.to_dict(only=['id', 'name', 'description']) for power in powers])

class PowerResource(Resource):
    def get(self, power_id):
        power = Power.query.get(power_id)
        if not power:
            return {"error": "Power not found"}, 404
        return jsonify(power.to_dict(only=['id', 'name', 'description']))

    def patch(self, power_id):
        power = Power.query.get(power_id)
        if not power:
            return {"error": "Power not found"}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True, help="Description is required")
        args = parser.parse_args()

        try:
            power.description = args['description']
            db.session.commit()
            return jsonify(power.to_dict(only=['id', 'name', 'description']))
        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400
