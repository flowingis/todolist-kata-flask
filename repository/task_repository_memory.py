from model.task import Task
from repository.task_repository import TaskRepository


class TaskRepositoryMemory(TaskRepository):
    def __init__(self):
        self.tasks = []

    def list(self) -> []:
        return self.tasks

    def get(self, task_id: str):
        filtered_list = [item for item in self.tasks if item.uuid == task_id]
        if len(filtered_list) == 1:
            return filtered_list[0]
        return None

    def add(self, new_task: Task) -> Task:
        self.tasks.insert(0, new_task)
        return new_task

    def update(self, task_id: str, new_task: Task):
        task_to_update = self.get(task_id)
        if task_to_update is None:
            raise Exception('Task not found: %s' % task_id)
        index = self.tasks.index(task_to_update)
        self.tasks[index].description = new_task.description

    def delete(self, task_id: str):
        task_to_delete = self.get(task_id)
        if task_to_delete is None:
            raise Exception('Task not found: %s' % task_id)
        self.tasks.remove(task_to_delete)

    def mark_as_done(self, task_id: str):
        task_to_update = self.get(task_id)
        if task_to_update is None:
            raise Exception('Task not found: %s' % task_id)
        index = self.tasks.index(task_to_update)
        self.tasks[index].done = 1
