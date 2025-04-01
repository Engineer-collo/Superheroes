from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)





# Join table for Hero and Power
class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_power"
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255), nullable=False)

    #validation
    @validates('strength')
    def validate_strength(self, key, value):
        strength = ["weak", "Average", "strong"]
        for n in strength:
            if value not in strength:
                raise ValueError(f"strength must be one of {strength}")


    # Relationships
    hero_id = db.Column(db.Integer, ForeignKey("heroes.id",ondelete="CASCADE" ), nullable=False)
    power_id = db.Column(db.Integer, ForeignKey("powers.id", ondelete="CASCADE"), nullable=False)

    # Set serialization rules
    serialize_rules = ("-hero.powers", "-power.heroes",)

    def __repr__(self):
        return f'< {self.strength}  {self.hero_id} {self.power_id}>'





# Hero model
class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)
        
    # Relationship   
    powers = db.relationship("Power", secondary="hero_power", cascade="all, delete", back_populates="heroes")

    # Set serialization rules
    serialize_rules = ("-powers.heroes",)



    def __repr__(self):
        return f'< {self.name}  {self.super_name}>'





# Power model
class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(300))

    #validation
    @validates('description')
    def validate_description(self, key, value):
        if not value.strip():
            raise ValueError("description can't be empty")

        if len(value) < 20:
            raise ValueError("description must be at least 20 characters long")
        return value

 
    heroes = db.relationship("Hero", secondary="hero_power",cascade="all, delete", back_populates="powers")

    # Set serialization rules
    serialize_rules = ("-heroes.powers",)


    def __repr__(self):
        return f'<Game {self.name} for {self.description}>'