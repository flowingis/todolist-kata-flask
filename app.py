from flask import Flask, render_template, jsonify
from flask_injector import FlaskInjector
from injector import inject

from dependencies import configure
from service.task_service import TaskService

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@inject
@app.route('/api/tasks')
def tasks_list(task_service: TaskService):
    return jsonify(task_service.list())


FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
