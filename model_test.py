import unittest
from src.predict import prediction
# from src.train import *



class BasicTests(unittest.TestCase):
    def test_Predict(self):
        result,score = prediction("test","data/tweets.csv","model/d2v.model")
        self.assertEqual(len(result),20)
        self.assertEqual(len(score),20)
        
    #def test_Train(self):
        #self.assertEqual(train("data/tweets.csv","model/test.model"),True)
        
if __name__ == '__main__':
    unittest.main()
