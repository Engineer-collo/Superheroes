
#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__) 
# Enable CORS for all routes


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

#Home route
@app.route('/')
def index():
    return make_response(jsonify({"message": "Welcome to the Hero API"}), 200)

#Get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_dict = [hero.to_dict() for hero in heroes]
    if not heroes:
        return make_response(jsonify({"message": "No heroes found"}), 404)
    return make_response(jsonify(heroes_dict), 200)

#Get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_dict = [power.to_dict() for power in powers]
    if not powers:
        return make_response(jsonify({"message": "No powers found"}), 404)
    return make_response(jsonify(powers_dict), 200)

#Get all hero-power relationships
@app.route('/hero-powers', methods=['GET'])
def get_hero_powers():
    hero_powers = HeroPower.query.all()
    hero_powers_dict = [hero_power.to_dict() for hero_power in hero_powers]
    if not hero_powers:
        return make_response(jsonify({"message": "No hero-powers found"}), 404)
    return make_response(jsonify(hero_powers_dict), 200)

#Get a hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return make_response(jsonify({"message": "Hero not found"}), 404)
    return make_response(jsonify(hero.to_dict()), 200)

#Get a power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response(jsonify({"message": "Power not found"}), 404)
    return make_response(jsonify(power.to_dict()), 200)

#PATCH a power by ID
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response(jsonify({"message": f"Power ID {id} not found"}), 404)
    
    data = request.get_json()
    power.name = data.get('name', power.name)
    power.description = data.get('description', power.description)
    db.session.commit()
    return make_response(jsonify(power.to_dict()), 200)

#POST heroPower
@app.route('/hero-power', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    # Validate Hero and Power existence
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero:
        return make_response(jsonify({"error": f"Hero ID {hero_id} not found"}), 404)
    if not power:
        return make_response(jsonify({"error": f"Power ID {power_id} not found"}), 404)

    # Validate Strength
    valid_strengths = ["Strong", "Weak", "Average"]
    if not strength or strength not in valid_strengths:
        return make_response(jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'."]}), 400)

    # Create HeroPower Relationship
    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    return make_response(jsonify(hero_power.to_dict()), 201)
