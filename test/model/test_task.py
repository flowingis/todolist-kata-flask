from unittest import TestCase

from model.task import Task


class TestTask(TestCase):
    def test_create(self):
        task = Task.create('test task')

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z')
        self.assertEqual('test task', task.description)

