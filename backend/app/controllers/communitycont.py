from flask import request, jsonify, abort
from app.models.community import CommunityPost
from app import db

def get_community_posts():
    community_posts = CommunityPost.query.all()
    return jsonify([community_post.serialize() for community_post in community_posts])

def get_community_post(community_post_id):
    community_post = CommunityPost.query.get_or_404(community_post_id)
    return jsonify(community_post.serialize())

def create_community_post():
    data = request.json

    # Basic validation  
    required_fields = ['user_id', 'content']
    for field in required_fields:
        if field not in data:
            abort(400, f'Missing required field: {field}')

    # Create a new community post
    new_community_post = CommunityPost(
        user_id=data['user_id'],
        content=data['content']
    )

    db.session.add(new_community_post)
    db.session.commit()

    return jsonify(new_community_post.serialize()), 201

def update_community_post(community_post_id):
    community_post = CommunityPost.query.get_or_404(community_post_id)
    data = request.json

    # Update fields if provided in the request
    for key, value in data.items():
        setattr(community_post, key, value)

    db.session.commit()

    return jsonify(community_post.serialize())

def delete_community_post(community_post_id):
    community_post = CommunityPost.query.get_or_404(community_post_id)
    db.session.delete(community_post)
    db.session.commit()

    return jsonify({'message': 'Community post deleted successfully'})
