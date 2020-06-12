from flask import Blueprint, jsonify, request, json
from injector import inject

from command.task_add_command import TaskAddCommand
from command.task_search_command import TaskSearchCommand
from command.task_update_command import TaskUpdateCommand
from model.task import Task
from service.task_service import TaskService

tasks_api = Blueprint('tasks_api', __name__)


@inject
@tasks_api.route('/api/tasks', methods=['GET'])
def tasks_list(task_service: TaskService) -> []:
    return jsonify(task_service.list())


@inject
@tasks_api.route('/api/tasks/<task_id>', methods=['GET'])
def tasks_get(task_service: TaskService, task_id: str):
    return jsonify(task_service.get(task_id))


@inject
@tasks_api.route('/api/tasks', methods=['POST'])
def tasks_add(task_service: TaskService) -> Task:
    command = TaskAddCommand.from_json_str(request.get_data())
    return jsonify(task_service.add(command))


@inject
@tasks_api.route('/api/tasks/<task_id>', methods=['PUT'])
def tasks_update(task_service: TaskService, task_id: str):
    command = TaskUpdateCommand.from_json_str(request.get_data())
    task_service.update(task_id, command)
    return '', 200


@inject
@tasks_api.route('/api/tasks/<task_id>', methods=['DELETE'])
def tasks_delete(task_service: TaskService, task_id: str):
    task_service.delete(task_id)
    return '', 200


@inject
@tasks_api.route('/api/tasks/<task_id>/done', methods=['POST'])
def tasks_done(task_service: TaskService, task_id: str):
    task_service.mark_as_done(task_id)
    return '', 200


@inject
@tasks_api.route('/api/tasks/<task_id>/undone', methods=['POST'])
def tasks_undone(task_service: TaskService, task_id: str):
    task_service.undone(task_id)
    return '', 200


@inject
@tasks_api.route('/api/tasks/search', methods=['GET'])
def tasks_search(task_service: TaskService):
    command = TaskSearchCommand.from_request(request.args)
    return jsonify(task_service.search(command))
