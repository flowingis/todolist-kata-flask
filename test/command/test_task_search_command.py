from unittest import TestCase

from command.task_search_command import TaskSearchCommand


class TestTask(TestCase):
    def test_from_request(self):
        request_data = {
            "description": "prova ricerca",
            "tags": "#abc, #def"
        }
        command = TaskSearchCommand.from_request(request_data)

        self.assertIsNotNone(command)
        self.assertEqual('prova ricerca', command.description)
        self.assertEqual(2, len(command.tags))
