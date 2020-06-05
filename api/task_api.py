from flask import Blueprint, jsonify, request, json
from injector import inject

from command.task_command import TaskCommand
from model.task import Task
from service.task_service import TaskService

tasks_api = Blueprint('tasks_api', __name__)


@inject
@tasks_api.route('/api/tasks', methods=['GET'])
def tasks_list(task_service: TaskService) -> []:
    return jsonify(task_service.list())


@inject
@tasks_api.route('/api/tasks', methods=['POST'])
def tasks_add(task_service: TaskService) -> Task:
    command = TaskCommand.from_json_str(request.get_data())
    return jsonify(task_service.add(command))
