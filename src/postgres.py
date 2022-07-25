from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin, CORS
from flask import Flask
from datetime import datetime



app = Flask(__name__)


db = SQLAlchemy(app)
class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(200), nullable = False)


    def __repr__(self):
        return "<Pet %r>" % self.pet_name

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    Full_Name = db. Column(db.String(100), nullable = False)
    Mobile_No = db.Column(db.Integer, nullable = False)
    Reg_No = db.Column(db.Integer, nullable = False)
    Branch = db.Column(db.String(100), nullable = False)
    Date_Created=db.Column(db.DateTime, default = datetime.now())


    def __repr__(self):
        return "<Student %r>" % self.Full_Name



