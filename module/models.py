from extensions import db
from flask_login import UserMixin
from sqlalchemy import inspect


# Model
class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(520), nullable=False)
    site_url = db.Column(db.String(520), nullable=False)
    site_password = db.Column(db.String(520), nullable=False)

    def __repr__(self):
        return f'<PasswordManager {self.email}>'



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(520))
    email = db.Column(db.String(520), nullable=False)
    password = db.Column(db.String(520), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


if __name__ == '__main__':
    pass