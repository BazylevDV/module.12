import unittest
from module2.tests_12_3 import RunnerTest, TournamentTest

# Создание TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuite
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запуск тестов
runner.run(suite)
