from flask import Blueprint, render_template

home = Blueprint('api', __name__)

@home.route('/')
def sitemap():
    return render_template("home.html")