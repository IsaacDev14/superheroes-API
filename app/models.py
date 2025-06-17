# app/models.py

from . import db  # Import the db object from __init__.py

class Hero(db.Model):
    """
    Hero model represents a superhero with a name and a super name.
    """
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # Relationship to HeroPower (one-to-many)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete")

    def to_dict(self):
        """
        Serialize Hero to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }
