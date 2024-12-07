import module_12
import unittest

from Module_12.module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner("Усейн", 10)
        self.run_2 = Runner("Андрей", 9)
        self.run_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)




    def test_run(self):
        tour_1 = Tournament(90,self.run_1 , self.run_3)
        self.all_results.update(tour_1.start())
        self.assertTrue(self.all_results[2], "Ник")

    def test_run_2(self):
        tour_2 = Tournament(90, self.run_2, self.run_3)
        self.all_results.update(tour_2.start())
        self.assertTrue(self.all_results[2], "Ник")

    def test_run_3(self):
        tour_3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results.update(tour_3.start())
        self.assertTrue(self.all_results[3], self.run_3)

if __name__ == "__main__":
    unittest.main()