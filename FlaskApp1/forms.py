from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    password_confirm = PasswordField("Confirm_Password", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")


class CalculatorForm(FlaskForm):
    num1 = IntegerField("First Number:", validators=[DataRequired()])
    num2 = IntegerField("Second Number:", validators=[DataRequired()])
    add = SubmitField("add")
    subtract = SubmitField("subtract")
    divide = SubmitField("divide")
    multiply = SubmitField("multiply")


class LetterForm(FlaskForm):
    word = StringField("Word", validators=[DataRequired()])
    submit = SubmitField("Submit")
