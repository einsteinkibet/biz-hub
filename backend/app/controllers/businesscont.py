from flask import request, jsonify, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
import logging
import os
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models.business import Business
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.INFO)

UPLOAD_FOLDER = 'business_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_error(e, status_code):
    logging.error(f'Error: {str(e)}')
    return jsonify({'error': str(e)}), status_code

def is_valid_business_name(name):
    # Implement your business name validation logic
    return 4 <= len(name) <= 50 and name.isalnum()

def business_name_exists(name):
    return db.session.query(Business.query.filter(func.lower(Business.name) == func.lower(name)).exists()).scalar()

def create_business():
    try:
        data = request.get_json()
        if 'name' not in data:
            return handle_error("Business name is required", 400)

        if not is_valid_business_name(data['name']):
            return handle_error("Invalid business name format", 400)

        if business_name_exists(data['name']):
            return handle_error("Business name already exists", 400)

        business_logo = data.get('logo')
        if business_logo and not allowed_file(business_logo['filename']):
            return handle_error("Invalid business logo file type", 400)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        if allowed_file(business_logo['filename']):
            filename = secure_filename(business_logo['filename'])
            business_logo.save(os.path.join(UPLOAD_FOLDER, filename))

        business = Business(
            name=data['name'],
            description=data.get('description'),
            owner_id=current_user.id,
            address=data.get('address'),
            contact_number=data.get('contact_number'),
            logo=filename if allowed_file(business_logo['filename']) else None,
            cover_image=data.get('cover_image')
        )

        db.session.add(business)
        db.session.commit()

        return jsonify({'message': 'Business created successfully'}), 201

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        db.session.rollback()
        return handle_error(e, 500)

def delete_business(id):
    try:
        business = Business.query.get_or_404(id)

        if not business.can_delete():
            flash('You are not authorized to delete this business.', 'danger')
            return redirect(url_for('business.index'))

        db.session.delete(business)
        db.session.commit()

        return jsonify({'message': 'Business deleted successfully'}), 200

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        db.session.rollback()
        return handle_error(e, 500)

def update_business(id):
    try:
        data = request.get_json()
        business = Business.query.get_or_404(id)

        if not business.can_edit():
            flash('You are not authorized to update this business.', 'danger')
            return redirect(url_for('business.index'))

        if 'name' in data:
            new_name = data['name']

            if not is_valid_business_name(new_name):
                return handle_error("Invalid business name format", 400)

            if new_name != business.name and business_name_exists(new_name):
                return handle_error("Business name already exists", 400)

            business.name = new_name

        # Update other fields as needed (description, address, contact_number, etc.)
        # ...

        db.session.commit()

        return jsonify({'message': 'Business updated successfully'}), 200

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        db.session.rollback()
        return handle_error(e, 500)

def get_business(id):
    try:
        business = Business.query.get_or_404(id)

        # Your business retrieval logic here
        # ...

        return jsonify(business.serialize()), 200

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        return handle_error(e, 500)

def get_businesses():
    try:
        businesses = Business.query.all()

        # Your business listing logic here
        # ...

        return jsonify([business.serialize() for business in businesses]), 200

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        return handle_error(e, 500)

# ... (Any other functions you may need)
