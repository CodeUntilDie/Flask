# coding: utf-8
from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    gender = db.Column(db.Boolean,)
    age = db.Column(db.Integer)
    created_date = db.Column(db.Integer)
    modified_date = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)

    def __init__(self, id, username, password, address, gender, age, created_date, modified_date, is_active):
        self.id = id
        self.username = username
        self.password = password
        self.address = address
        self.gender = gender
        self.age = age
        self.created_date = created_date
        self.modified_date = modified_date
        self.is_active = is_active

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def save_data(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "username": self.username,
            "password": self.password,
            "address": self.address,
            "gender": self.gender,
            "age": self.age,
            "create_date": self.create_date,
            "modified_date": self.modified_date,
            "is_active": self.is_active
        }

    def delete_data(self):
        db.session.delete()
        db.session.commit()

    def save_changes(self):
        db.session.commit()

