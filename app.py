import os
from flask import Flask, render_template, redirect, url_for
# Database related imports:
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Form related imports:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'
app.config["TEMPLATES_AUTO_RELOAD"] = True

##########################################
############ DATABASE SETUP ##############
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

##########################################
### DEFINE A MODEL (DATABASE TABLE) ######
##########################################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # initialise an instance (row) of a table/entity
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

##########################################
### SIMPLE FORM TO CREATE NEW USER #######
##########################################

class CreateUser(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    submit = SubmitField("Create user")

##########################################
########## VIEW (CONTROLLER) #############
##########################################

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CreateUser()
    if form.validate_on_submit():
        # Crete a new user with the submitted info from the form:
        user = User(email=form.email.data,
                    name = form.name.data)

        # To update the database:
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))
    return (render_template('index.html', form=form))

@app.route('/users')
def users():
    # Query the database:
    users_list = User.query.all()
    return render_template('users.html', users_list=users_list)
