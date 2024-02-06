from flask import jsonify, request
from app.models.reviews import Review
from app import db

def create_review(user_id, business_id, rating, comment):
    try:
        new_review = Review(
            user_id=user_id,
            business_id=business_id,
            rating=rating,
            comment=comment
        )

        db.session.add(new_review)
        db.session.commit()

        return jsonify({'message': 'Review created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_reviews():
    reviews = Review.query.all()
    serialized_reviews = [review.serialize() for review in reviews]
    return jsonify(serialized_reviews)

def get_review(review_id):
    review = Review.query.get(review_id)
    if review:
        return jsonify(review.serialize())
    else:
        return jsonify({'message': 'Review not found'}), 404

def update_review(review_id):
    try:
        review = Review.query.get(review_id)
        if not review:
            return jsonify({'message': 'Review not found'}), 404

        data = request.json
        review.rating = data.get('rating', review.rating)
        review.comment = data.get('comment', review.comment)

        db.session.commit()

        return jsonify({'message': 'Review updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def delete_review(review_id):
    try:
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return jsonify({'message': 'Review deleted successfully'}), 200
        else:
            return jsonify({'message': 'Review not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
