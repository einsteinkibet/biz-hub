from flask import request, jsonify
import logging
from email_validator import validate_email, EmailNotValidError
from sqlalchemy.exc import SQLAlchemyError
import os 
from werkzeug.utils import secure_filename
from app import db


logging.basicConfig(level = logging.INFO)

UPLOAD_FOLDER = 'profile_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def handle_error(e,status_code):
    logging.error(f'Error:{str(e)}')
    return jsonify({'error':str(e)}), status_code

def is_valid_email(email):
    try:
        # Validate email using email_validator library
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False
    
def username_exists(username):
    # Check if the username already exists in the database
    return db.session.query(User.query.filter_by(username=username).exists()).scalar()


from app.models.user import User
def create_user():
    try:
        data = request.get_json()
        if 'username' not in data or 'password' not in data:
        
            missing_fields = []
            if 'username' not in data:
                missing_fields.append('username')
            if 'email' not in data or not data['email']:
                missing_fields.append('email')
            elif not is_valid_email(data['email']):
                return handle_error("Invalid email format", 400)

            if 'password' not in data:
                missing_fields.append('password')
        
            error_message = f"Missing required fields: {', '.join(missing_fields)}"
            return handle_error(error_message)
        
        if len(data['username']) < 4 or len(data['username']) > 20:
            return handle_error("Username must be between 4 and 20 characters", 400)
        
        if len(data['password']) < 8:
            return handle_error("Password must be at least 8 characters", 400)
        
        if username_exists(data['username']):
            return handle_error("Username already exists", 400)


        profile_pic = data['profile_picture']
        if not allowed_file(profile_pic['filename']):
            return handle_error("Invalid profile picture file type", 400)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        if allowed_file(profile_pic['filename']):
            filename = secure_filename(profile_pic['filename'])
            profile_pic.save(os.path.join(UPLOAD_FOLDER, filename))
            user.profile_picture = filename

        user = User(username=data['username'], email = data['email'], password = data['password'], profile_picture = data['profile_picture'])
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        db.session.rollback()  # Rollback the changes in case of an error
        return handle_error(e, 500)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def login(username, password):
    user = get_user_by_username(username)

    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

def get_users():
    try:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        username = request.json.get('username')
        password = request.json.get('password')

        if username:
            user.username = username
        if password:
            user.password = generate_password_hash(password, method='sha256')

        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)