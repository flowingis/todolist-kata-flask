from unittest import TestCase

from repository.task_repository_memory import TaskRepositoryMemory
from service.task_service import TaskService


class TestTaskService(TestCase):
    def setUp(self) -> None:
        task_repository: TaskRepositoryMemory = TaskRepositoryMemory()
        self.task_service = TaskService(task_repository)

    def test_list(self):
        tasks: [] = self.task_service.list()

        self.assertEqual(2, len(tasks))
