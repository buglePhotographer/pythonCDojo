'''
Created on Dec 8, 2014

@author: gustavo.citati
'''
import unittest
from src import romanNumerals


class Test(unittest.TestCase):

    #global x

    def setUp(self):
        #global x = romanNumerals.romanNumerals(self)
        pass


    def tearDown(self):
        pass


    def test_one(self):
        x = romanNumerals.romanNumerals(self)
        self.assertEqual(x.ConvertToArabic('I'), 1)
        
    def test_two(self):
        x = romanNumerals.romanNumerals(self)
        self.assertEqual(x.ConvertToArabic('V'), 5)
        self.assertEqual(x.ConvertToArabic('X'), 10)
        self.assertEqual(x.ConvertToArabic('L'), 50)
        self.assertEqual(x.ConvertToArabic('C'), 100)
        self.assertEqual(x.ConvertToArabic('D'), 500)
        self.assertEqual(x.ConvertToArabic('M'), 1000)
        
    def test_three(self):
        x = romanNumerals.romanNumerals(self)
        self.assertEqual(x.ConvertToArabic('II'), 2)
        
    def test_four(self):
        x = romanNumerals.romanNumerals(self)
        self.assertEqual(x.ConvertToArabic('III'), 3)
        self.assertEqual(x.ConvertToArabic('XXX'), 30)
        self.assertEqual(x.ConvertToArabic('CCC'), 300)
        self.assertEqual(x.ConvertToArabic('MMM'), 3000)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()