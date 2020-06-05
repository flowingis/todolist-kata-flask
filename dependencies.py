from injector import singleton

from repository.task_repository import TaskRepository
from repository.task_repository_memory import TaskRepositoryMemory
from service.task_service import TaskService


def configure(binder):
    binder.bind(TaskService, to=TaskService, scope=singleton)
    binder.bind(TaskRepository, to=TaskRepositoryMemory, scope=singleton)
