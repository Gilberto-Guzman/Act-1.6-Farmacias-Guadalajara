from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("views/home/home.html")


@views.route("/contact")
def contact():
    return render_template("views/contact/contact.html")


@views.route("/login")
def login():
    return render_template("views/login/login.html")


@views.route("/register")
def register():
    return render_template("views/register/register.html")
