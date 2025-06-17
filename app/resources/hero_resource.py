from flask_restful import Resource, reqparse
from ..models import Hero, db

# Request parser for Hero inputs
hero_parser = reqparse.RequestParser()
hero_parser.add_argument("name", required=True, help="Hero name is required")
hero_parser.add_argument("super_name", required=True, help="Super name is required")

class HeroListResource(Resource):
    def get(self):
        """
        Get all heroes.
        """
        heroes = Hero.query.all()
        return [{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes], 200

    def post(self):
        """
        Create a new hero.
        """
        args = hero_parser.parse_args()
        new_hero = Hero(name=args["name"], super_name=args["super_name"])
        db.session.add(new_hero)
        db.session.commit()
        return {"message": "Hero created", "id": new_hero.id}, 201

class HeroResource(Resource):
    def get(self, id):
        """
        Get a single hero by ID.
        """
        hero = Hero.query.get_or_404(id)
        return {"id": hero.id, "name": hero.name, "super_name": hero.super_name}, 200

    def delete(self, id):
        """
        Delete a hero.
        """
        hero = Hero.query.get_or_404(id)
        db.session.delete(hero)
        db.session.commit()
        return {"message": "Hero deleted"}, 204
