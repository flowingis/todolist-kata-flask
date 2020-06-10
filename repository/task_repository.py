from abc import abstractmethod, ABC

from command.task_add_command import TaskAddCommand
from model.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def list(self) -> []:
        pass

    @abstractmethod
    def get(self, task_id: str):
        pass

    @abstractmethod
    def add(self, new_task: Task) -> Task:
        pass

    @abstractmethod
    def update(self, task_id: str, new_task: Task):
        pass

    @abstractmethod
    def delete(self, task_id: str):
        pass

    @abstractmethod
    def mark_as_done(self, task_id: str):
        pass
