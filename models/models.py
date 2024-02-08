from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData, event
from sqlalchemy_serializer import SerializerMixin
import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from services import db, bcrypt


class Animal():
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    feed = db.Column(db.String)
    img = db.Column(db.String)
    pass

class Farmer():
    __tablename__ = "farmers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    # favorite_animal = db.Column(db.String)
    pass

class Farm():
    __tablename__ = "farms"
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'))
    name = db.Column(db.String)
    # img = db.Column(db.String)
    # total_animals = db.Column(db.Integer)
    # total_farmers = db.Column(db.Integer)
    # year_of_establishment = db.Column(db.String)
    pass