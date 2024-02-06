from datetime import datetime
from flask import jsonify
from app.models.promotions import Promotion
from app import db

def create_promotion(business_id, title, description, start_date, end_date, user_id):
    try:
        new_promotion = Promotion(
            business_id=business_id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id
        )

        db.session.add(new_promotion)
        db.session.commit()

        return jsonify({'message': 'Promotion created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_promotions():
    promotions = Promotion.query.all()
    serialized_promotions = [promotion.serialize() for promotion in promotions]
    return jsonify(serialized_promotions)

def delete_expired_promotions():
    current_datetime = datetime.utcnow()

    expired_promotions = Promotion.query.filter(Promotion.end_date <= current_datetime).all()

    for promotion in expired_promotions:
        db.session.delete(promotion)

    db.session.commit()

# Add other functions for getting, updating, and deleting promotions if needed
# ...
