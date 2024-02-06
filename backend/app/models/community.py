from app import db

class CommunityPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'content':self.content
        }