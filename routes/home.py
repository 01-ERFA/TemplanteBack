from flask import Blueprint, render_template
from models.tasks import Task

home = Blueprint('api', __name__)

@home.route('/')
def sitemap():
    return render_template("home.html")

