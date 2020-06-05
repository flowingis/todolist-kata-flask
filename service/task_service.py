from flask import jsonify
from injector import inject

from command.task_add_command import TaskAddCommand
from model.task import Task
from repository.task_repository import TaskRepository


class TaskService:

    @inject
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def list(self) -> []:
        return self.task_repository.list()

    def add(self, command: TaskAddCommand) -> Task:
        assert command is not None

        return self.task_repository.add(command)

    def delete(self, task_id: str):
        assert task_id is not None

        self.task_repository.delete(task_id)
