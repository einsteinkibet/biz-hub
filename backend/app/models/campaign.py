from app import db

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return{
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'start_date':self.start_date,
            'end_date':self.end_date
        }