#!/usr/bin/env python3

# Standard library imports
from flask import request, jsonify, make_response
from flask_cors import CORS
# Local imports
from config import app, db, api
from models import User, PriceRanges, BuildComponents, Builds, GPU, CPU, Memory, MotherBoard, Storage, PSU, Case, BuildType
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
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    
    if user:
        builds = Builds.query.filter_by(price_range_id=user.selected_price_range).all()
        
        build_details_list = []
        
        for build in builds:
            components_record = BuildComponents.query.filter_by(build_id=build.id).first()
            build_type = db.session.get(BuildType, build.build_type_id)
            price_range = PriceRanges.query.get(build.price_range_id)

            full_components = {
                'gpu': db.session.get(GPU, components_record.gpu_id).serialize(),
                'cpu': db.session.get(CPU, components_record.cpu_id).serialize(),
                'memory': db.session.get(Memory, components_record.memory_id).serialize(),
                'motherboard': db.session.get(MotherBoard, components_record.motherboard_id).serialize(),
                'storage': db.session.get(Storage, components_record.storage_id).serialize(),
                'psu': db.session.get(PSU, components_record.psu_id).serialize(),
                'case': db.session.get(Case, components_record.case_id).serialize(),

            }

            build_details_list.append({
                'build_id': build.id,
                'price_range': f"{price_range.min_price}-{price_range.max_price}", 
                'build_type': build_type.type_name, 
                'components': full_components
            })
        
        return jsonify(build_details_list)
    else:
        return jsonify({'error': 'User not found'}), 404
    
@app.route('/get_builds', methods=['GET'])
def get_builds():
    min_price = request.args.get('minPrice')
    max_price = request.args.get('maxPrice')
    
    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    price_range = PriceRanges.query.filter(
        PriceRanges.min_price <= min_price, 
        PriceRanges.max_price >= max_price
    ).first()
    
    if price_range is None:
        return jsonify({'error': 'No matching price range found'}), 400

    builds = Builds.query.filter_by(price_range_id=price_range.id).all()

    build_details_list = []
    for build in builds:
        components_record = BuildComponents.query.filter_by(build_id=build.id).first()
        build_type = db.session.get(BuildType, build.build_type_id)
        price_range = PriceRanges.query.get(build.price_range_id)

        full_components = {
            'gpu': db.session.get(GPU, components_record.gpu_id).serialize(),
            'cpu': db.session.get(CPU, components_record.cpu_id).serialize(),
            'memory': db.session.get(Memory, components_record.memory_id).serialize(),
            'motherboard': db.session.get(MotherBoard, components_record.motherboard_id).serialize(),
            'storage': db.session.get(Storage, components_record.storage_id).serialize(),
            'psu': db.session.get(PSU, components_record.psu_id).serialize(),
            'case': db.session.get(Case, components_record.case_id).serialize(),
        }

        build_details_list.append({
            'id': build.id,
            'price_range_id': build.price_range_id,
            'price_range': f"{price_range.min_price}-{price_range.max_price}",
            'build_type': build_type.type_name,
            'build_type_id': build.build_type_id,
            'components': full_components  
        })

    return jsonify({'builds': build_details_list})  

@app.route('/get_parts', methods=['GET'])
def get_parts():
    type_ = request.args.get('type')
    print(f"Received type_: {type_}")  

    if type_ is None:
        return jsonify({'error': 'Type is missing'}), 400

    type_ = type_.lower()  
    
    if type_ == 'gpu':
        parts = GPU.query.all()
    elif type_ == 'cpu':
        parts = CPU.query.all()
    elif type_ == 'memory':
        parts = Memory.query.all()
    elif type_ == 'motherboard':
        parts = MotherBoard.query.all()
    elif type_ == 'storage':
        parts = Storage.query.all()
    elif type_ == 'psu':
        parts = PSU.query.all()
    elif type_ == 'case':
        parts = Case.query.all()
    else:
        return jsonify({'error': f'Invalid type: {type_}'}), 400  # Detailed error message

    return jsonify([part.serialize() for part in parts])

@app.route('/save_build', methods=['POST'])
def save_build():
    username = request.cookies.get('username') 
    if not username:
        return jsonify({'message': 'Not authenticated'}), 401

    build_details = request.json.get('build')

    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    new_build = Builds(
        price_range_id=build_details.get('price_range_id'),
        build_type_id=build_details.get('build_type_id')
    )

    new_build.user_id = user.id
    
    db.session.add(new_build)
    db.session.commit()
    
    return jsonify({'message': 'Build saved successfully'})

    

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
