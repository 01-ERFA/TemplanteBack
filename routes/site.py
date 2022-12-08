from flask import Blueprint, render_template

home = Blueprint('home', __name__)
docs = Blueprint('docs', __name__)
test = Blueprint('test', __name__)

@home.route('/')
def sitemap():
    return render_template('home.html')


@docs.route('/docs')
def docs_page():
    return render_template('docs.html')

@test.route('/testing')
def test_api():
    return render_template('test.html')