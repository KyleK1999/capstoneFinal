#!/usr/bin/env python3

# Standard library imports
from flask import request, jsonify, make_response
from flask_restful import Resource
from scraper import run_scraper 
# Local imports
from config import app, db, api
from models import User
import bcrypt


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


@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    run_scraper()
    app.run(port=5555, debug=True)



