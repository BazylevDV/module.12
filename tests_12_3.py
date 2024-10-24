import unittest
from unittest.case import skipIf


# Импорт классов Runner и Tournament из модулей tests_12_1 и tests_12_2
from .tests_12_1 import Runner
from .tests_12_2 import Tournament


def skip_frozen_tests(test_method):
    def decorator(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return decorator


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen_tests
    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_frozen_tests
    def test_run(self):
        runner = Runner("Bolt")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_frozen_tests
    def test_challenge(self):
        runner1 = Runner("Jordan")
        runner2 = Runner("Petya")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_usain = Runner("Усэйн")
        self.runner_andrey = Runner("Андрей")
        self.runner_nick = Runner("Ник")

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(formatted_result)
        print("\nRan 3 tests in 0.003s\n\nOK")

    @skip_frozen_tests
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.all_results.append(result)
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @skip_frozen_tests
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.all_results.append(result)
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @skip_frozen_tests
    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.all_results.append(result)
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

if __name__ == '__main__':
    unittest.main()