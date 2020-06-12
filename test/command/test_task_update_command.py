from unittest import TestCase

from command.task_update_command import TaskUpdateCommand


class TestTask(TestCase):
    def test_from_json_str(self):
        json_str = '{"description":"nuovo task", "tags":"#abd #def"}'
        command = TaskUpdateCommand.from_json_str(json_str)

        self.assertIsNotNone(command)
        self.assertEqual('nuovo task', command.description)
        self.assertEqual(2, len(command.tags))
