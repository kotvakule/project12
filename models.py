from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    price = db.Column(db.Float, nullable=False)

class User2(db.Model):
    id1 = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.Text(), nullable=True)
    login = db.Column(db.Text(), nullable=True)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))