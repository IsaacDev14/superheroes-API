#app/seed.py
from random import choice as rc
from . import create_app, db
from .models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    ]
    db.session.add_all(powers)

    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]
    db.session.add_all(heroes)

    strengths = ["Strong", "Weak", "Average"]
    hero_powers = [
        HeroPower(hero=hero, power=rc(powers), strength=rc(strengths))
        for hero in heroes
    ]
    db.session.add_all(hero_powers)
    db.session.commit()
    print("✅ Database seeded!")

