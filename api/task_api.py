from flask import Blueprint, jsonify, request, json
from injector import inject

from command.task_add_command import TaskAddCommand
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
    command = TaskAddCommand.from_json_str(request.get_data())
    return jsonify(task_service.add(command))


@inject
@tasks_api.route('/api/tasks/<task_id>', methods=['DELETE'])
def tasks_delete(task_service: TaskService, task_id: str):
    task_service.delete(task_id)
    return '', 200
