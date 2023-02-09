from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")


@views.route("/home")
def home():
    return render_template("views/home/home.html")


@views.route("/contact")
def contact():
    return render_template("views/contact/contact.html")
