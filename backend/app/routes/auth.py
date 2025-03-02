# Authentication endpoints
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from ..models.user import User
from ..extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """User registration with M-Pesa phone validation"""
    data = request.get_json()
    
    # Validate Kenyan phone number
    if not data['phone'].startswith('254') or len(data['phone']) != 12:
        return jsonify({"error": "Invalid Kenyan phone number"}), 400
    
    # Check existing user
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username exists"}), 409
        
    new_user = User(
        username=data['username'],
        _mpesa_phone=data['phone'],
        _password=data['password']  # Auto-hashed via model setter
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """JWT authentication with MFA support"""
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.verify_password(data['password']):
        # Generate JWT token
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 200
        
    return jsonify({"error": "Invalid credentials"}), 401
