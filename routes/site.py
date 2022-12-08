from flask import Blueprint, render_template

site = Blueprint('site', __name__)


@site.route('/')
def sitemap():
    return render_template('home.html')


@site.route('/docs')
def docs_page():
    return render_template('docs.html')

@site.route('/testing')
def test_api():
    return render_template('test.html')