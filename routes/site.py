from flask import Blueprint, render_template, redirect, request
from models.tasks import Task
from utils.session import session


site = Blueprint('site', __name__)

@site.route('/')
def sitemap():
    return render_template('home.html')


@site.route('/docs')
def docs_page():
    return render_template('docs.html')

@site.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return render_template('test.html', tasks=tasks)

@site.route('/tasks', methods=['POST'])
def save_tasks():
    new_task = Task(title=request.form['title'], description=request.form['description'])
    
    session.add(new_task)
    session.commit()
    tasks = Task.query.all()
    return render_template('test.html', tasks=tasks)