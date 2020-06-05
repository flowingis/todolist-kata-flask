import unittest

testmodules = [
    'test.model.test_task',
    'test.service.test_task_service',
    'test.command.test_task_command'
]


def suite():
    suite = unittest.TestSuite()

    for t in testmodules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
