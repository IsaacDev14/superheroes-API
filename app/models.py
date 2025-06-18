from .extensions import db
from sqlalchemy.orm import validates

# Simple serialization mixin to control output
class SerializeMixin:
    def to_dict(self, only=None, exclude=None, recurse=1):
        """Serialize model to dict with control on recursion depth"""
        d = {}
        for column in self.__table__.columns:
            if only and column.name not in only:
                continue
            if exclude and column.name in exclude:
                continue
            d[column.name] = getattr(self, column.name)
        
        if recurse > 0:
            for rel in self.__mapper__.relationships:
                if only and rel.key not in only:
                    continue
                if exclude and rel.key in exclude:
                    continue
                related_obj = getattr(self, rel.key)
                if related_obj is None:
                    d[rel.key] = None
                elif rel.uselist:
                    d[rel.key] = [o.to_dict(recurse=recurse-1) for o in related_obj]
                else:
                    d[rel.key] = related_obj.to_dict(recurse=recurse-1)
        return d

class Hero(db.Model, SerializeMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    # Relationship to HeroPower (one-to-many)
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

class Power(db.Model, SerializeMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)

    # Relationship to HeroPower (one-to-many)
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    # Validation: description must be present and at least 20 chars
    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description

class HeroPower(db.Model, SerializeMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(10), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    # Validation: strength must be Strong, Weak or Average
    @validates('strength')
    def validate_strength(self, key, strength):
        allowed = ['Strong', 'Weak', 'Average']
        if strength not in allowed:
            raise ValueError(f"Strength must be one of {allowed}")
        return strength
