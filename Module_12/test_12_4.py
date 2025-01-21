import logging
import module_12_4
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = module_12_4.Runner('name', -10)
            logging.info(f'"test_walk" выполнен успешно')
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 100)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            runner2 = module_12_4.Runner(1)
            logging.info(f'"test_run" выполнен успешно')
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)



    def test_challenge(self):
        runner3 = module_12_4.Runner('name3')
        runner4 = module_12_4.Runner('name3')
        for _ in range(5):
            runner3.run()
        for _ in range(5):
            runner3.walk()
        self.assertNotEqual(runner4.distance, runner3.distance)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding="utf - 8", format="%(asctime)s | %(levelname)s | %(message)s")

    