from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biz-hub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bcrypt.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
    return app