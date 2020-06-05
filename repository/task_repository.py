from abc import abstractmethod, ABC

from command.task_add_command import TaskAddCommand
from model.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def list(self) -> []:
        pass

    @abstractmethod
    def add(self, command: TaskAddCommand) -> Task:
        pass

    @abstractmethod
    def delete(self, task_id: str):
        pass
