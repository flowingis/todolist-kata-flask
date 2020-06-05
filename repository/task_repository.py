from abc import abstractmethod, ABC

from command.task_command import TaskCommand
from model.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def list(self) -> []:
        pass

    @abstractmethod
    def add(self, command: TaskCommand) -> Task:
        pass
