from flask import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    full_name = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256),nullable=False)


    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password
