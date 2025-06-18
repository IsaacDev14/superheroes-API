from flask_restful import Resource
from flask import request
from ..models import HeroPower, Hero, Power, db

class HeroPowerCreateResource(Resource):
    def post(self):
        data = request.get_json()

        try:
            # Create a new HeroPower record from JSON
            new_hp = HeroPower(
                strength=data["strength"],
                hero_id=data["hero_id"],
                power_id=data["power_id"]
            )

            db.session.add(new_hp)
            db.session.commit()

            # Fetch related Hero and Power to return full context
            hero = Hero.query.get(data["hero_id"])
            power = Power.query.get(data["power_id"])

            return {
                **new_hp.to_dict(),
                "hero": hero.to_dict(),
                "power": power.to_dict()
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400
