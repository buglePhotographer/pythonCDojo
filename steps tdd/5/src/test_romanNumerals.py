'''
Created on Dec 8, 2014

@author: gustavo.citati
'''
from src import romanNumerals
import unittest



class Test(unittest.TestCase):

    x = romanNumerals.romanNumerals()

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_one(self):
        self.assertEqual(self.x.ConvertToArabic('I'), 1)
        
    def test_two(self):
        self.assertEqual(self.x.ConvertToArabic('V'), 5)
        self.assertEqual(self.x.ConvertToArabic('X'), 10)
        self.assertEqual(self.x.ConvertToArabic('L'), 50)
        self.assertEqual(self.x.ConvertToArabic('C'), 100)
        self.assertEqual(self.x.ConvertToArabic('D'), 500)
        self.assertEqual(self.x.ConvertToArabic('M'), 1000)
        
    def test_three(self):
        self.assertEqual(self.x.ConvertToArabic('II'), 2)
        
    def test_four(self):
        self.assertEqual(self.x.ConvertToArabic('III'), 3)
        self.assertEqual(self.x.ConvertToArabic('XXX'), 30)
        self.assertEqual(self.x.ConvertToArabic('CCC'), 300)
        self.assertEqual(self.x.ConvertToArabic('MMM'), 3000)
        
    def test_five(self):
        self.assertEqual(self.x.ConvertToArabic('IIII'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('VV'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('XXXX'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('LL'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('CCCC'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('DD'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('IIIV'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('MMMMM'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('DM'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('XXL'), "Not a valid number")
        self.assertEqual(self.x.ConvertToArabic('VVX'), "Not a valid number")
        
    def test_six(self):
        self.assertEqual(self.x.ConvertToArabic('MD'), 1500)
        self.assertEqual(self.x.ConvertToArabic('MMD'), 2500)
        self.assertEqual(self.x.ConvertToArabic('VIII'), 8)
        self.assertEqual(self.x.ConvertToArabic('xl'), 40)
        self.assertEqual(self.x.ConvertToArabic('CD'), 400)
        self.assertEqual(self.x.ConvertToArabic('xCviii'), 98)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()