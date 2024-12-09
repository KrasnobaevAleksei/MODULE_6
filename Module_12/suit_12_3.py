import unittest
import test_12_3


testing = unittest.TestSuite()

testing.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))

testing.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(testing)