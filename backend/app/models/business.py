from app import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    contact_number = db.Column(db.String(15), nullable=True)
    logo = db.Column(db.String(100), nullable=True)
    cover_image = db.Column(db.String(100), nullable=True)
    promotions = db.relationship('Promotion', backref='business', lazy=True)
    reviews = db.relationship('Review', backref='business', lazy=True)

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'owner_id':self.owner_id,
            'address':self.address,
            'contact_number':self.contact_number,
            'logo':self.logo,
            'cover_image':self.cover_image
        }