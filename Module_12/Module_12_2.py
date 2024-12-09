import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results={}
        
    def setUp(self):
        self.first_runner=runner_and_tournament.Runner("Усэйн", 10)
        self.second_runner=runner_and_tournament.Runner("Андрей", 9)
        self.third_runner=runner_and_tournament.Runner("Ник", 3)
        
    @classmethod
    def tearDownClass(cls):
        for p in cls.all_results:
            print("{",end="")
            for key in cls.all_results[p]:
                print(str(key) + ":",str(cls.all_results[p][key]), " " ,end="")
            print("}")
     
    def test_first_run(self):
        t=runner_and_tournament.Tournament(90,self.first_runner,self.third_runner)
        self.all_result=t.start()
        self.all_results["test_1"]=self.all_result
        self.assertTrue(self.all_result[len(self.all_result)-1],"Ник")

    def test_second_run(self):
        t=runner_and_tournament.Tournament(90,self.second_runner,self.third_runner)
        self.all_result=t.start()
        self.all_results["test_2"]=self.all_result
        self.assertTrue(self.all_result[len(self.all_result)-1],"Ник")

    def test_third_run(self):
        t=runner_and_tournament.Tournament(90,self.first_runner,self.second_runner,self.third_runner)
        self.all_result=t.start()
        self.all_results["test_3"]=self.all_result
        self.assertTrue(str(self.all_result[len(self.all_result)-1]),"Ник")

if __name__=="__main__":
    unittest.main()

"""По поводу ошибки не особо корректно сравнивать пройденную дистанцию с заданной
так как пройденная может оказаться больше чем заданная таким образом если 
взять короткую дистанцию (меньше его скорости) и первым отправить тихохода то он выиграет
необходимо сравнивать время или в нашел случае дистанции между собой (правильно ли я понял?)"""