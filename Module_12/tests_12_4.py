import rt_with_exceptions
import unittest
import logging

class RunnerTest(unittest.TestCase):
    
    is_frozen = False
       
    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        try: 
            run=rt_with_exceptions.Runner("Milka",-5)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance,-50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            run=rt_with_exceptions.Runner(["Burenka"])
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance,100)
            logging.info("'test_run' выполнен успешно")
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_challenge(self):
        run1=rt_with_exceptions.Runner("Milka")
        run2=rt_with_exceptions.Runner("Burenka")
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance,run2.distance)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()