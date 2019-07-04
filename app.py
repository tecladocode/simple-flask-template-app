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
    return render_template("home.html", name=session.get("username", "Unknown"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username][1] == password:
            session["username"] = username
            return redirect(url_for("home"))
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
