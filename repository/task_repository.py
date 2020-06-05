from abc import abstractmethod, ABC


class TaskRepository(ABC):

    @abstractmethod
    def list(self):
        pass
