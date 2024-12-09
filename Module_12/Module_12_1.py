import runner
import unittest

class RunnerTest(unittest.TestCase):
    
    def test_walk(self):
        run=runner.Runner("Milka")
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance,50)

    def test_run(self):
        run=runner.Runner("Burenka")
        for _ in range(10):
            run.run()
        #Хороший тест
        self.assertEqual(run.distance,100)
        #ошибка
        #self.assertEqual(run.distance,110)

    def test_challenge(self):
        run1=runner.Runner("Milka")
        run2=runner.Runner("Burenka")
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance,run2.distance)

if __name__=="__main__":
    unittest.main()