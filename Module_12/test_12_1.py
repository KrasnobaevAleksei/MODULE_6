import module_12
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = module_12.Runner('name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner2 = module_12.Runner('name2')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)
    def test_challenge(self):
        runner3 = module_12.Runner('name3')
        runner4 = module_12.Runner('name3')
        for _ in range(5):
            runner3.run()
        for _ in range(5):
            runner3.walk()
        self.assertNotEqual(runner4.distance, runner3.distance)

if __name__ == "__main__":
    unittest.main()