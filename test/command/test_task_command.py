from unittest import TestCase

from command.task_add_command import TaskAddCommand


class TestTask(TestCase):
    def test_from_json_str(self):
        json_str = '{"description":"nuovo task"}'
        command = TaskAddCommand.from_json_str(json_str)

        self.assertIsNotNone(command)
        self.assertEqual('nuovo task', command.description)
