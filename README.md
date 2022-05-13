# Flask models

### App structure

Now that we have several "moving parts", I have made this app fairly simple, with form, model and controller (@route) in app.py. In a real app consider moving the model into its own models.py file (or even have separate models.py files for each part of the application, as demonstrated in [flask-blueprints](https://github.com/ChristinaVoss/flask-blueprints).


<img width="632" alt="Screenshot 2022-05-12 at 09 39 07" src="https://user-images.githubusercontent.com/20923607/168029239-c23abd0c-cd5f-421a-8c99-3570209aeb19.png">

**Key parts**

In app.py:

Import your installed libraries related to database and migrations:

```
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
```
Configure your database (set data path etc), and define a variable to use for your database queries (db):

```
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
```

Define your database table (called model, though defined as a Python class and inherits from db.Model). Include an `__init__()` method to initialise your objects and and a `__repr__()` method to give your bojects a string representation (so you can print them...):

```
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
```

At the bottom of your model definitions (if you have more than one), add this line to create the tables:

`db.create_all()`

You can now create a user in @app.route('/'):

```
user = User(email=form.email.data,
            name = form.name.data)

# To add a row to the User table in the database:
db.session.add(user)
db.session.commit()
```

And query the database as seen in @app.route('/users'):

`users_list = User.query.all()`

### Setup

If you have not installed Python3, [please do](https://www.python.org/downloads/).

First create and activate some form of environment to store your dependencies. I like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html):

```
$ conda create -n myenv python=3.7

$ conda activate myenv
```

**Or** just use Pythons built in environments:

```
$ python3 -m venv venv

$ . venv/bin/activate
```

Then install Flask, Flask-SQLAlchemy, Flask-Migrate, and also WTForms (because we added a form to update the database).

`$ pip install Flask Flask-WTF Flask-SQLAlchemy Flask-Migrate`

### Run the app

`$ flask run`

You should now be able to see the output in your browser window (at http://127.0.0.1:5000) 

### Resulting pages

**index.html**

<img width="522" alt="Screenshot 2022-05-12 at 18 05 26" src="https://user-images.githubusercontent.com/20923607/168130267-85438f4c-7ea6-4ec5-98f4-b825c29ee6b6.png">


**users.html**

<img width="519" alt="Screenshot 2022-05-12 at 18 05 47" src="https://user-images.githubusercontent.com/20923607/168130279-0a65d6d6-c838-4248-bf5b-e12318ea7778.png">






