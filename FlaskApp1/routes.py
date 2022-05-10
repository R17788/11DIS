from FlaskApp1 import app, db
from flask import render_template, request, redirect, flash
from FlaskApp1.models import User, Course, Enrolments
from FlaskApp1.forms import LoginForm, RegisterForm


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return "<h1>Hello Everyone!!</h1>"
    return render_template("index.html", login=False, index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password) == user.password:
            flash(f"{user.first_name}, you are successfully logged in!")
            return redirect("/index")
        else:
            flash("Sorry, Something went wrong.")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/courses")
def courses():
    courseData = [
        {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
         "term": "Spring"},
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
         "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                           "term": "Fall, Spring"},
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
         "term": "Fall"}]
    print(type(courseData))
    print(courseData)
    return render_template("courses.html", courseData=courseData, courses=True)


@app.route("/enrolment", methods=['GET', 'POST'])
def enrolment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrolment.html", register=True, data={"id": id, "title": title, "term": term})


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(user_id=user, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route("/user")
def user():
    # User(user_id=1, first_name="Ryan", last_name="Hawcroft", email="ryan@sps.com.au", password="abc1234").save()
    # User(user_id=2, first_name="Connor", last_name="Lowe", email="connor@sps.com.au", password="password123").save()
    # Users = User.object.all()
    return render_template("user.html")


@app.route("/calculator")
def calculator():
    numbers = [
        {"num1": 6},
        {"num2": 4},
    ]
    print(numbers)
    return render_template("calculator.html")
