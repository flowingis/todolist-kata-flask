import unittest

testmodules = [
    'test.model.test_task',
    'test.model.test_task_query_data',
    'test.service.test_task_service',
    'test.command.test_task_add_command',
    'test.command.test_task_update_command',
    'test.command.test_task_search_command'
]


def suite():
    suite = unittest.TestSuite()

    for t in testmodules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
