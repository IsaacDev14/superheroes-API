from flask_restful import Resource
from ..models import Hero

class HeroListResource(Resource):
    def get(self):
        # Return a list of all heroes
        heroes = Hero.query.all()
        return [h.to_dict() for h in heroes], 200

class HeroDetailResource(Resource):
    def get(self, id):
        # Return a specific hero with their powers
        hero = Hero.query.get(id)
        if not hero:
            return {"error": "Hero not found"}, 404

        data = hero.to_dict()

        # Include all powers associated with the hero
        data["hero_powers"] = [
            {
                **hp.to_dict(),
                "power": hp.power.to_dict()
            }
            for hp in hero.hero_powers
        ]

        return data, 200
