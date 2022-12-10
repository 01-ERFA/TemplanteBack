from flask import Blueprint, render_template, redirect, request
from models.tasks import Task
from utils.setup import session


site = Blueprint('site', __name__)

@site.route('/')
def sitemap():
    return render_template('home.html')


@site.route('/docs')
def docs_page():
    return render_template('docs.html')

@site.route('/testing', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return render_template('test.html', tasks=tasks)

@site.route('/testing', methods=['POST'])
def save_tasks():
    new_task = Task(title=request.form['title'], description=request.form['description'])
    
    session.add(new_task)
    session.commit()
    return redirect('/testing')