#app/routes/hero.py

from flask_restful import Resource
from ..models import Hero

class HeroListResource(Resource):
    def get(self):
        heroes = Hero.query.all()
        return [h.to_dict() for h in heroes], 200

class HeroDetailResource(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {"error": "Hero not found"}, 404
        data = hero.to_dict()
        data["hero_powers"] = [
            {
                **hp.to_dict(),
                "power": hp.power.to_dict()
            }
            for hp in hero.hero_powers
        ]
        return data, 200
