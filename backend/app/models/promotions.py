from app import db

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return{
            'id':self.id,
            'business_id':self.business_id,
            'title':self.title,
            'description':self.description,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'user_id':self.user_id
        }