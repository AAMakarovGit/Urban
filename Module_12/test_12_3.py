import unittest
import Module_12_1_1
import Module_12_2_1

test_suite=unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1_1.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)