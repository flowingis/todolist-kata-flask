from flask import Flask, render_template
from flask_injector import FlaskInjector

from api.task_api import tasks_api
from dependencies import configure

app = Flask(__name__)
app.register_blueprint(tasks_api)


@app.route('/')
def home():
    return render_template('home.html')


FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
