'''
Created on Dec 8, 2014

@author: gustavo.citati
'''
import unittest
from src import romanNumerals


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_one(self):
        x = romanNumerals.romanNumerals(self)
        self.assertEqual(x.ConvertToArabic('I'), 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()