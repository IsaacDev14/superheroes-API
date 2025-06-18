#app/routes/power.py

from flask_restful import Resource
from flask import request
from ..models import Power, db

class PowerListResource(Resource):
    def get(self):
        powers = Power.query.all()
        return [p.to_dict() for p in powers], 200

class PowerDetailResource(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404
        return power.to_dict(), 200

class PowerUpdateResource(Resource):
    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404

        data = request.get_json()
        try:
            if "description" in data:
                power.description = data["description"]
            db.session.commit()
            return power.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400
