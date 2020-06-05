import uuid

from model.task import Task
from repository.task_repository import TaskRepository


class TaskRepositoryMemory(TaskRepository):

    def __init__(self):
        self.tasks = [
            Task.create("Primo"),
            Task.create("Secondo")
        ]

    def list(self) -> []:
        return self.tasks
