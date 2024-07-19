from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date


db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first = db.Column(db.String(50))
    last = db.Column(db.String(50))
    password = db.Column(db.String(128))
    email = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(14))
    hobby = db.Column(db.String(255), nullable=True)
    # profile_picture = db.Column(db.String(20), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"