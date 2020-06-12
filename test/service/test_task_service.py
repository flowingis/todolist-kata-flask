from unittest import TestCase

from command.task_add_command import TaskAddCommand
from command.task_search_command import TaskSearchCommand
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
        command = TaskAddCommand(description='nuovo task', tags=['#abc', '#def'])
        task: Task = self.task_service.add(command)
        num_tasks_after_insert: int = len(self.task_service.list())

        self.assertIsNotNone(task)
        self.assertRegex(task.uuid, r'%s' % UUID4_REGEX)
        self.assertEqual(command.description, task.description)
        self.assertEqual(1, num_tasks_after_insert)
        self.assertEqual(2, len(task.tags))

    def test_delete_with_empty_id_should_throw_exception(self):
        with self.assertRaises(AssertionError):
            self.task_service.delete(None)

    def test_delete_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            self.task_service.delete('xxxx')

    def test_delete_with_valid_id_should_remove_the_right_task(self):
        command = TaskAddCommand(description='nuovo task', tags=[])
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
        add_command = TaskAddCommand(description='nuovo task', tags=[])
        task: Task = self.task_service.add(add_command)
        uuid_to_update = task.uuid
        update_command = TaskUpdateCommand(description='task modificato', tags=['#abc'])
        self.task_service.update(uuid_to_update, update_command)
        read_task: Task = self.task_service.get(uuid_to_update)

        self.assertEqual('task modificato', read_task.description)
        self.assertEqual(1, len(read_task.tags))
        self.assertEqual('#abc', read_task.tags[0])

    def test_done_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            self.task_service.mark_as_done('xxxx')

    def test_done_with_valid_id_should_update_the_right_task(self):
        add_command = TaskAddCommand(description='nuovo task', tags=[])
        task: Task = self.task_service.add(add_command)
        uuid_to_update = task.uuid
        self.task_service.mark_as_done(uuid_to_update)
        read_task: Task = self.task_service.get(uuid_to_update)

        self.assertEqual(1, read_task.done)

    def test_undone_with_non_valid_id_should_throw_exception(self):
        with self.assertRaises(Exception):
            self.task_service.undone('xxxx')

    def test_undone_with_valid_id_should_update_the_right_task(self):
        add_command = TaskAddCommand(description='nuovo task', tags=[])
        task: Task = self.task_service.add(add_command)
        uuid_to_update = task.uuid

        self.task_service.mark_as_done(uuid_to_update)
        read_task_before_undone: Task = self.task_service.get(uuid_to_update)
        done_state_before_undone = read_task_before_undone.done

        self.task_service.undone(uuid_to_update)
        read_task_after_undone: Task = self.task_service.get(uuid_to_update)
        done_state_after_undone = read_task_after_undone.done

        self.assertEqual(1, done_state_before_undone)
        self.assertEqual(0, done_state_after_undone)

    def test_search_with_empty_query_data_should_return_entire_list(self):
        self.task_service.add(
            TaskAddCommand(description='primo task', tags=['#abc', '#def'])
        )
        self.task_service.add(
            TaskAddCommand(description='secondo task', tags=['#abc'])
        )

        search_command = TaskSearchCommand(description='', tags=[])
        filtered_tasks = self.task_service.search(search_command)

        self.assertEqual(2, len(filtered_tasks))

    def test_search_description_should_return_filtered_list(self):
        self.task_service.add(
            TaskAddCommand(description='primo task', tags=['#abc', '#def'])
        )
        self.task_service.add(
            TaskAddCommand(description='secondo task', tags=['#abc'])
        )

        search_command = TaskSearchCommand(description='primo', tags=[])
        filtered_tasks = self.task_service.search(search_command)

        self.assertEqual(1, len(filtered_tasks))
        self.assertEqual('primo task', filtered_tasks[0].description)

    def test_search_tags_should_return_filtered_list(self):
        self.task_service.add(
            TaskAddCommand(description='primo task', tags=['#abc', '#def', '#ghi'])
        )
        self.task_service.add(
            TaskAddCommand(description='secondo task', tags=['#abc', '#zxc'])
        )

        search_command = TaskSearchCommand(description='', tags=['#abc', '#def'])
        filtered_tasks = self.task_service.search(search_command)

        self.assertEqual(1, len(filtered_tasks))
        self.assertEqual('primo task', filtered_tasks[0].description)

    def test_search_description_and_tags_should_return_filtered_list(self):
        self.task_service.add(
            TaskAddCommand(description='primo task', tags=['#abc', '#def', '#ghi'])
        )
        self.task_service.add(
            TaskAddCommand(description='secondo task', tags=['#abc', '#zxc'])
        )

        search_command = TaskSearchCommand(description='primo', tags=['#abc', '#def'])
        filtered_tasks = self.task_service.search(search_command)

        self.assertEqual(1, len(filtered_tasks))
        self.assertEqual('primo task', filtered_tasks[0].description)
