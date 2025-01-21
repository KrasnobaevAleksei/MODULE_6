
import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
#
# class RunnerTest(unittest.TestCase):
#     def test_walk(self):
#         runner = Runner('name')
#         for _ in range(10):
#             runner.walk()
#         self.assertEqual(runner.distance, 50)
#     def test_run(self):
#         runner2 = Runner('name2')
#         for _ in range(10):
#             runner2.run()
#         self.assertEqual(runner2.distance, 100)
#     def test_challenge(self):
#         runner3 = Runner('name3')
#         for _ in range(5):
#             runner3.run()
#         for _ in range(5):
#             runner3.walk()
#         self.assertNotEqual(runner3.distance, 140)
# if __name__ == "__main__":
#         unittest.main()
