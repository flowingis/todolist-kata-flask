from unittest import TestCase

from command.task_command import TaskCommand
from model.task import Task
from repository.task_repository_memory import TaskRepositoryMemory
from service.task_service import TaskService

UUID4_REGEX = r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z'


class TestTaskService(TestCase):
    def setUp(self) -> None:
        task_repository: TaskRepositoryMemory = TaskRepositoryMemory()
        self.task_service = TaskService(task_repository)

    def test_list_should_return_empty_array(self):
        tasks: [] = self.task_service.list()

        self.assertEqual(0, len(tasks))

    def test_add_should_return_just_created_task(self):
        command = TaskCommand(description='nuovo task')
        task: Task = self.task_service.add(command)

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'%s' % UUID4_REGEX)
        self.assertEqual(command.description, task.description)
