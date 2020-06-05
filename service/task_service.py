from flask import jsonify
from injector import inject

from command.task_command import TaskCommand
from model.task import Task
from repository.task_repository import TaskRepository


class TaskService:

    @inject
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def list(self) -> []:
        return self.task_repository.list()

    def add(self, command: TaskCommand) -> Task:
        return self.task_repository.add(command)
