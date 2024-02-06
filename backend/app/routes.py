from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.controllers.usercont import create_user, get_users, get_user, update_user, delete_user, get_user_by_username, login
from app.controllers.promotionscont import create_promotion, get_promotions, delete_expired_promotions
from app.controllers.reviewcont import create_review, get_reviews, get_review, update_review, delete_review
from app.controllers.communitycont import (
    get_community_posts,
    get_community_post,
    create_community_post,
    update_community_post,
    delete_community_post,
)
from app.controllers.businesscont import (
    create_business,
    get_businesses,
    get_business,
    update_business,
    delete_business,
)

bp = Blueprint('bp', __name__)

# User routes
@bp.route('/user', methods=['POST'])
def add_user_route():
    data = request.json
    username = data.get('username', '')
    existing_user = get_user_by_username(username)

    if existing_user:
        return jsonify({'message': 'Error: Username already exists. Please choose another username.'}), 400

    if len(username) < 5:
        return jsonify({'message': 'Error: Username must be at least 5 characters.'}), 400

    response, status_code = create_user()
    return jsonify(response), status_code

@bp.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin()
def login_():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight request handled'}), 200

    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    return login(username, password)

@bp.route('/user', methods=['GET'])
def get_users_route():
    return get_users()

@bp.route('/user/<int:id>')
def get_user_route(id):
    return get_user(id)

@bp.route('/user/<int:id>', methods=['PUT', 'PATCH'])
def update_user_route(id):
    return update_user(id)

@bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    return delete_user(id)

# Business routes
@bp.route('/business', methods=['POST'])
def add_business_route():
    return create_business()

@bp.route('/business')
def get_businesses_route():
    return get_businesses()

@bp.route('/business/<int:id>')
def get_business_route(id):
    return get_business(id)

@bp.route('/business/<int:id>', methods=['PUT', 'PATCH'])
def update_business_route(id):
    return update_business(id)

@bp.route('/business/<int:id>', methods=['DELETE'])
def delete_business_route(id):
    return delete_business(id)

# Promotions routes
@bp.route('/promotion', methods=['POST'])
def add_promotion_route():
    return create_promotion()

@bp.route('/promotion')
def get_promotions_route():
    return get_promotions()

@bp.route('/promotion/delete-expired', methods=['DELETE'])
def delete_expired_promotions_route():
    delete_expired_promotions()
    return jsonify({'message': 'Expired promotions deleted successfully'}), 200

# Review routes
@bp.route('/review', methods=['POST'])
@cross_origin()
def add_review_route():
    return create_review()

@bp.route('/review')
def get_reviews_route():
    return get_reviews()

@bp.route('/review/<int:id>')
def get_review_route(id):
    return get_review(id)

@bp.route('/review/<int:id>', methods=['PUT', 'PATCH'])
def update_review_route(id):
    return update_review(id)

@bp.route('/review/<int:id>', methods=['DELETE'])
def delete_review_route(id):
    return delete_review(id)

# Community routes
@bp.route('/community-posts', methods=['GET'])
def get_community_posts_route():
    return get_community_posts()

@bp.route('/community-posts/<int:community_post_id>')
def get_community_post_route(community_post_id):
    return get_community_post(community_post_id)

@bp.route('/community-posts', methods=['POST'])
def create_community_post_route():
    return create_community_post()

@bp.route('/community-posts/<int:community_post_id>', methods=['PUT', 'PATCH'])
def update_community_post_route(community_post_id):
    return update_community_post(community_post_id)

@bp.route('/community-posts/<int:community_post_id>', methods=['DELETE'])
def delete_community_post_route(community_post_id):
    return delete_community_post(community_post_id)
