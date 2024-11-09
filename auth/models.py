from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# Define the User model
class User(UserMixin, db.Model):
    __tablename__ = 'UserAuth'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key, auto-incremented
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username (unique)
    password = db.Column(db.String(200), nullable=False)  # Hashed password
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email (unique)

    def __repr__(self):
        return f'<User {self.username}>'
