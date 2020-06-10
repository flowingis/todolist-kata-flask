from unittest import TestCase

from command.task_add_command import TaskAddCommand
from command.task_update_command import TaskUpdateCommand
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

    def test_add_with_empty_command_should_throw_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.task_service.add(None)

    def test_add_should_return_just_created_task(self):
        command = TaskAddCommand(description='nuovo task')
        task: Task = self.task_service.add(command)
        num_tasks_after_insert: int = len(self.task_service.list())

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'%s' % UUID4_REGEX)
        self.assertEqual(command.description, task.description)
        self.assertEqual(1, num_tasks_after_insert)

    def test_delete_with_empty_id_should_throw_exception(self):
        with self.assertRaises(AssertionError):
            self.task_service.delete(None)

    def test_delete_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            self.task_service.delete('xxxx')

    def test_delete_with_valid_id_should_remove_the_right_task(self):
        command = TaskAddCommand(description='nuovo task')
        task: Task = self.task_service.add(command)
        num_tasks_after_insert: int = len(self.task_service.list())
        uuid_to_delete = task.uuid
        self.task_service.delete(uuid_to_delete)
        num_tasks_after_delete: int = len(self.task_service.list())

        self.assertEqual(1, num_tasks_after_insert)
        self.assertEqual(0, num_tasks_after_delete)

    def test_update_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            command = TaskUpdateCommand(description='task modificato')
            self.task_service.update('xxxx', command)

    def test_update_with_valid_id_should_update_the_right_task(self):
        add_command = TaskAddCommand(description='nuovo task')
        task: Task = self.task_service.add(add_command)
        uuid_to_update = task.uuid
        update_command = TaskUpdateCommand(description='task modificato')
        self.task_service.update(uuid_to_update, update_command)
        read_task: Task = self.task_service.get(uuid_to_update)

        self.assertEqual('task modificato', read_task.description)

    def test_done_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            command = TaskUpdateCommand(description='task modificato')
            self.task_service.mark_as_done('xxxx')

    def test_done_with_valid_id_should_update_the_right_task(self):
        add_command = TaskAddCommand(description='nuovo task')
        task: Task = self.task_service.add(add_command)
        uuid_to_update = task.uuid
        self.task_service.mark_as_done(uuid_to_update)
        read_task: Task = self.task_service.get(uuid_to_update)

        self.assertEqual(1, read_task.done)
