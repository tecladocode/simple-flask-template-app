"""
This app is only partially complete. At the moment we can't sign up or log in new users.

Want to find out how we'd complete it?

Check out our blog post: <>
"""
import functools
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "jose"

users = {"jose": ("jose", "1234")}


def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return secure_function


@app.route("/")
def home():
    return render_template("home.html", name=session.get("username", "Unknown"))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=session["username"])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        next_url = request.form.get("next")

        if username in users and users[username][1] == password:
            session["username"] = username
            if next_url:
                return redirect(next_url)
            return redirect(url_for("profile"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in users:
            users[username] = (username, password)
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))
