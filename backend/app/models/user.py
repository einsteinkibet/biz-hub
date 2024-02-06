from flask import flash
from app import db, bcrypt
from sqlalchemy.orm import validates

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable =False)
    email = db.Column(db.String(30), nullable = False, unique = True)
    _password = db.Column(db.String(60), nullable=False)
    # role = db.Column(db.String(20), nullable=False, default='user')
    profile_picture = db.Column(db.String(100), nullable=True)
    businesses = db.relationship('Business', backref='owner', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    posts = db.relationship('CommunityPost', backref='user', lazy=True)

    @property
    def password(self):
        return self._password
    
    def set_password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    @password.setter
    def password(self, plaintext_password):
        self.set_password(plaintext_password)

    def check_password(self, plaintext_password):
        return self.check_password_hash(self._password, plaintext_password)
    
    def serialize(self):
        return {
            'id': self.id,
            'username':self.username,
            'email':self.email,
            'password':self._password.decode('utf-8') if isinstance(self._password, bytes) else self._password,
            'profile_picture': self.profile_picture
        }