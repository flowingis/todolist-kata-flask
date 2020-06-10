from flask import jsonify
from injector import inject

from command.task_add_command import TaskAddCommand
from command.task_update_command import TaskUpdateCommand
from model.task import Task
from repository.task_repository import TaskRepository


class TaskService:

    @inject
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def list(self) -> []:
        return self.task_repository.list()

    def get(self, task_id: str) -> Task:
        assert task_id is not None
        return self.task_repository.get(task_id)

    def add(self, command: TaskAddCommand) -> Task:
        assert command is not None
        return self.task_repository.add(Task.from_command(command))

    def update(self, task_id: str, command: TaskUpdateCommand):
        assert task_id is not None
        assert command is not None
        self.task_repository.update(task_id, Task.from_command(command))

    def delete(self, task_id: str):
        assert task_id is not None
        self.task_repository.delete(task_id)

    def mark_as_done(self, task_id: str):
        assert task_id is not None
        self.task_repository.mark_as_done(task_id)
