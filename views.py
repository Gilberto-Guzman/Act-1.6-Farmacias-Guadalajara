from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")


@views.route("/home")
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
