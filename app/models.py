# app/models.py
from app.database import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class Hero(db.Model, SerializerMixin):
    """Hero model representing a superhero."""
    __tablename__ = 'heroes'
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    # Relationships
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')
    
    # Serialization rules to limit recursion
    serialize_rules = ('-hero_powers.hero',)
    
    def __repr__(self):
        return f'<Hero {self.super_name}>'

class Power(db.Model, SerializerMixin):
    """Power model representing a superpower."""
    __tablename__ = 'powers'
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    # Relationships
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')
    
    # Serialization rules to limit recursion
    serialize_rules = ('-hero_powers.power',)
    
    # Validations
    @validates('description')
    def validate_description(self, key, description):
        """Ensure description is present and at least 20 characters long."""
        if not description or len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long')
        return description
    
    def __repr__(self):
        return f'<Power {self.name}>'

class HeroPower(db.Model, SerializerMixin):
    """HeroPower model representing the relationship between Hero and Power."""
    __tablename__ = 'hero_powers'
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    
    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    
    # Serialization rules to limit recursion
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')
    
    # Validations
    @validates('strength')
    def validate_strength(self, key, strength):
        """Ensure strength is one of 'Strong', 'Weak', or 'Average'."""
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError(f'Strength must be one of: {", ".join(valid_strengths)}')
        return strength
    
    def __repr__(self):
        return f'<HeroPower hero_id={self.hero_id} power_id={self.power_id} strength={self.strength}>'