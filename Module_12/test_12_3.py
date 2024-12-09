import module_12
import unittest
from Module_12.module_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = module_12.Runner('name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner2 = module_12.Runner('name2')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner3 = module_12.Runner('name3')
        runner4 = module_12.Runner('name3')
        for _ in range(5):
            runner3.run()
        for _ in range(5):
            runner3.walk()
        self.assertNotEqual(runner4.distance, runner3.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner("Усейн", 10)
        self.run_2 = Runner("Андрей", 9)
        self.run_3 = Runner("Ник", 3)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        tour_1 = Tournament(90,self.run_1 , self.run_3)
        self.all_results.update(tour_1.start())
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run_2(self):
        tour_2 = Tournament(90, self.run_2, self.run_3)
        self.all_results.update(tour_2.start())
        self.assertTrue(self.all_results[len(self.all_results)] =="Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run_3(self):
        tour_3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results.update(tour_3.start())
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

if __name__ == "__main__":
    unittest.main()