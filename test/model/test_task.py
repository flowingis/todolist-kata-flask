from unittest import TestCase

from command.task_command import TaskCommand
from model.task import Task

UUID4_REGEX = r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z'


class TestTask(TestCase):
    def test_create(self):
        task = Task.create('test task')

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'%s' % UUID4_REGEX)
        self.assertEqual('test task', task.description)

    def test_from_command(self):
        command = TaskCommand(description='nuovo task')
        task = Task.from_command(command)

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'%s' % UUID4_REGEX)
        self.assertEqual(command.description, task.description)
