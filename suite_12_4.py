import unittest
from module.tests_12_4 import RunnerTest


# Создание TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuite
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

# Создание объекта TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запуск тестов
runner.run(suite)

