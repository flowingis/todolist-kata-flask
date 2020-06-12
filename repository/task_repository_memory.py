from model.task import Task
from model.task_query_data import TaskQueryData
from repository.task_repository import TaskRepository


class TaskRepositoryMemory(TaskRepository):
    def __init__(self):
        self.tasks = []
        self.filtered_tasks = []

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
        self.tasks[index].tags = list(new_task.tags)

    def delete(self, task_id: str):
        task_to_delete = self.get(task_id)
        if task_to_delete is None:
            raise Exception('Task not found: %s' % task_id)
        self.tasks.remove(task_to_delete)

    def mark_as_done(self, task_id: str):
        self.__update_done_state(task_id, 1)

    def undone(self, task_id: str):
        self.__update_done_state(task_id, 0)

    def __update_done_state(self, task_id: str, done):
        task_to_update = self.get(task_id)
        if task_to_update is None:
            raise Exception('Task not found: %s' % task_id)
        index = self.tasks.index(task_to_update)
        self.tasks[index].done = done

    def search(self, query_data: TaskQueryData):
        self.filtered_tasks = list([item for item in self.tasks if self.__filter_query(item, query_data)])
        return self.filtered_tasks

    def __filter_query(self, task: Task, query_data: TaskQueryData):
        if query_data.description and not query_data.description.lower() in task.description.lower():
            return False

        if len(query_data.tags) > 0 and not set(query_data.tags).issubset(set(task.tags)):
            return False

        return True
