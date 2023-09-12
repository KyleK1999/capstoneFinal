#!/usr/bin/env python3

# Standard library imports
from flask import request, jsonify, make_response, Flask
from flask_restful import Resource
from flask_cors import CORS
# Local imports
from config import app, db, api
from models import User, PriceRanges, BuildComponents, Builds
import bcrypt

CORS(app, supports_credentials=True)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password=hashed_pw.decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered!'})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        resp = make_response(jsonify({'message': 'Logged in successfully!'}))
        resp.set_cookie('username', username)
        return resp

    return jsonify({'message': 'Invalid username or password'}), 401

def find_price_range_id(min_price, max_price):
    price_range = PriceRanges.query.filter_by(min_price=min_price, max_price=max_price).first()
    return price_range.id if price_range else None


@app.route('/set_price_range', methods=['POST'])
def set_price_range():
    username = request.json.get('username')
    min_price = request.json.get('selected_price_range').get('min_price')
    max_price = request.json.get('selected_price_range').get('max_price')

    user = User.query.filter_by(username=username).first()

    if user:
        # Using the function to find the price range ID
        price_range_id = find_price_range_id(min_price, max_price)
        
        if price_range_id:
            # Updating the user's selected price range
            user.selected_price_range = price_range_id
            db.session.commit()
            return jsonify({'message': 'Price range updated successfully'})
        
        return jsonify({'message': 'Price range not found'}), 404
        
    return jsonify({'message': 'User not found'}), 404

@app.route('/get_builds_for_user', methods=['GET'])
def get_builds_for_user():
    username = request.args.get('username')  # get this from username cookie in real application
    user = User.query.filter_by(username=username).first()
    
    if user:
        builds = Build.query.filter_by(price_range_id=user.selected_price_range).all()
        
        build_components_list = []
        for build in builds:
            components = BuildComponents.query.filter_by(build_id=build.id).first()
            build_components_list.append(components.serialize())  # Assuming you have a serialize method to convert object to JSON
        
        return jsonify(build_components_list)
    else:
        return jsonify({'error': 'User not found'}), 404



@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
