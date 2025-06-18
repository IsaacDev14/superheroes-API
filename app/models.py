from app import db
from sqlalchemy.orm import validates

# Mixin class to convert model instances to dicts
class SerializeMixin:
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Hero model
class Hero(db.Model, SerializeMixin):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    # One-to-many relationship to HeroPower
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete')

# Power model
class Power(db.Model, SerializeMixin):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete')

    # Validation: description must be at least 20 characters
    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value

# HeroPower join model (many-to-many with extra fields)
class HeroPower(db.Model, SerializeMixin):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    # Validation: only allow predefined strength values
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return value
