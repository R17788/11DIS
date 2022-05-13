import flask
from FlaskApp1 import db


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


class Course(db.Document):
    courseID = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_lenght=100)
    description = db.StringField(max_length=255)
    credits = db.IntField()
    term = db.StringField(max_length=25)


class Enrolment(db.Document):
    user_id = db.IntField()
    courseID = db.StringField(max_length=10)


class Calculator(db.Document):
    num1 = db.IntField()
    num2 = db.IntField()
