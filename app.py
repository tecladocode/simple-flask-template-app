"""
This app is only partially complete. At the moment we can't sign up or log in new users.

Want to find out how we'd complete it?

Check out our blog post: <>
"""

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "jose"

users = {"jose": ("jose", "1234")}


@app.route("/")
def home():
    return render_template("home.jinja2", name=session.get("username", "Unknown"))


@app.route("/login")
def login():
    return render_template("login.jinja2")


@app.route("/register")
def register():
    # Here you could register the user.
    # Add them to a database, for example.
    return render_template("register.jinja2")
