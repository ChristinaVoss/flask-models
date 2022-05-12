# Flask models

### App structure

Now that we have several "moving parts", I have made this app fairly simple, with form, model and controller (@route) in app.py. In a real app consider moving the model into its own models.py file (or even have separate models.py files for each part of the application, as demonstrated in [flask-blueprints](https://github.com/ChristinaVoss/flask-blueprints).


<img width="632" alt="Screenshot 2022-05-12 at 09 39 07" src="https://user-images.githubusercontent.com/20923607/168029239-c23abd0c-cd5f-421a-8c99-3570209aeb19.png">


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






