from command.task_command import TaskCommand
from model.task import Task
from repository.task_repository import TaskRepository


class TaskRepositoryMemory(TaskRepository):
    def __init__(self):
        self.tasks = []

    def list(self) -> []:
        return self.tasks

    def add(self, command: TaskCommand) -> Task:
        new_task = Task.from_command(command)
        self.tasks.append(new_task)
        return new_task
