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
        return '<PasswordManager %r>' % self.email



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(520))
    email = db.Column(db.String(520), nullable=False)
    password = db.Column(db.String(520), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email


if __name__ == '__main__':
    ...
    # dados = PasswordManager.query.all()
    # for i in dados:
    #     print(i)
    
    # mapper = inspect(PasswordManager)
    # for column in mapper.attrs:
    #     print(column.key)
        
    
    # colunas = PasswordManager.__table__.columns
    # for i in colunas:
    #     print(i)
    
    # print(list(i for i in PasswordManager.__table__.columns))