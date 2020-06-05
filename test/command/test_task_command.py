from unittest import TestCase

from command.task_command import TaskCommand


class TestTask(TestCase):
    def test_from_json_str(self):
        json_str = '{"description":"nuovo task"}'
        command = TaskCommand.from_json_str(json_str)

        self.assertIsNotNone(command)
        self.assertEqual('nuovo task', command.description)
