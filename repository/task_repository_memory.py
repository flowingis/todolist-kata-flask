from command.task_add_command import TaskAddCommand
from model.task import Task
from repository.task_repository import TaskRepository


class TaskRepositoryMemory(TaskRepository):
    def __init__(self):
        self.tasks = []

    def list(self) -> []:
        return self.tasks

    def add(self, command: TaskAddCommand) -> Task:
        new_task = Task.from_command(command)
        self.tasks.append(new_task)
        return new_task

    def delete(self, task_id: str):
        task_to_delete = self.get_by_id(task_id)
        if task_to_delete is None:
            raise Exception('Task not found: %s' % task_id)
        self.tasks.remove(task_to_delete)

    def get_by_id(self, task_id: str):
        filtered_list = [item for item in self.tasks if item.uuid == task_id]
        if len(filtered_list) == 1:
            return filtered_list[0]
        return None
