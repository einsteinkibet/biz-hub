from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'business_id':self.business_id,
            'rating':self.rating,
            'comment':self.comment
        }