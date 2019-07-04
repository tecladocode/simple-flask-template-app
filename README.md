# Simple Flask Template App

This short code repository shows how a Flask application that serves HTML files may be created.

It is used in our blog post, "How to add user logins to your Flask website". Read that for more info!

## Installing

You'll need `flask` to run this code sample. Install it like so:

```
pipenv install flask
```

## The app

Creating a Flask app is simple. Here we create one and also give it a `secret_key`. This is used for securing the cookies that the Flask app sends to each user.

```python
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "jose"
```

## The users

In this Flask application we have a list of users. We use these to implement authentication (login and signup) in the app. We do that in the blog post.

```python
users = {"jose": ("jose", "1234")}
```

This is a mapping of usernames to user data. This allows us to access `users[username]` when a user sends us their username.

It means we won't have to search through a list of users when we get a user's username.

## The routes

We have three pages in this starter app: `home`, `login`, and `register`.

At the moment these only return HTML pages (from the `templates` folder). In the blog post we modify two of them to actually deal with user data.

```python
@app.route("/")
def home():
    return render_template("home.jinja2")


@app.route("/login")
def login():
    # Here you could deal with the user's username and password.
    # Check if they're correct.
    return render_template("login.jinja2")


@app.route("/register")
def register():
    # Here you could register the user.
    # Add them to a database, for example.
    return render_template("register.jinja2")
```

## Running the app

To run this app, enter the Pipenv shell and run the app via the Flask CLI. Make sure you're in the correct directory first:

```
pipenv shell
flask run
```