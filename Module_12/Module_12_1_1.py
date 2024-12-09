import runner
import unittest

class RunnerTest(unittest.TestCase):
    
    is_frozen = False
       
    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        run=runner.Runner("Milka")
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance,50)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_run(self):
        run=runner.Runner("Burenka")
        for _ in range(10):
            run.run()
        #Хороший тест
        self.assertEqual(run.distance,100)
        #ошибка
        #self.assertEqual(run.distance,110)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_challenge(self):
        run1=runner.Runner("Milka")
        run2=runner.Runner("Burenka")
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance,run2.distance)

if __name__=="__main__":
    unittest.main()