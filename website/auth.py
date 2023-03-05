from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("views/login/login.html")


@auth.route("/register")
def register():
    return render_template("views/register/register.html")
