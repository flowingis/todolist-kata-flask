from unittest import TestCase

from command.task_search_command import TaskSearchCommand
from model.task_query_data import TaskQueryData


class TestTask(TestCase):
    def test_from_command(self):
        command = TaskSearchCommand(description='nuovo task', tags=['#abc', '#def'])
        query_data = TaskQueryData.from_command(command)

        self.assertIsNotNone(query_data)
        self.assertEqual(command.description, query_data.description)
        self.assertEqual(2, len(query_data.tags))
        self.assertEqual('#abc', query_data.tags[0])
        self.assertEqual('#def', query_data.tags[1])
