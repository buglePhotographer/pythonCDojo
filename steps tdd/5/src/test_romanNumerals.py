'''
Created on Dec 8, 2014

@author: gustavo.citati
'''
from src import romanNumerals
import unittest



class Test(unittest.TestCase):

    #global x

    def setUp(self):
        #global x = romanNumerals.romanNumerals(self)
        pass


    def tearDown(self):
        pass


    def test_one(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('I'), 1)
        
    def test_two(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('V'), 5)
        self.assertEqual(x.ConvertToArabic('X'), 10)
        self.assertEqual(x.ConvertToArabic('L'), 50)
        self.assertEqual(x.ConvertToArabic('C'), 100)
        self.assertEqual(x.ConvertToArabic('D'), 500)
        self.assertEqual(x.ConvertToArabic('M'), 1000)
        
    def test_three(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('II'), 2)
        
    def test_four(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('III'), 3)
        self.assertEqual(x.ConvertToArabic('XXX'), 30)
        self.assertEqual(x.ConvertToArabic('CCC'), 300)
        self.assertEqual(x.ConvertToArabic('MMM'), 3000)
        
    def test_five(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('IIII'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('VV'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('XXXX'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('LL'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('CCCC'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('DD'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('IIIV'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('MMMMM'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('DM'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('XXL'), "Not a valid number")
        self.assertEqual(x.ConvertToArabic('VVX'), "Not a valid number")
        
    def test_six(self):
        x = romanNumerals.romanNumerals()
        self.assertEqual(x.ConvertToArabic('MD'), 1500)
        self.assertEqual(x.ConvertToArabic('MMD'), 2500)
        self.assertEqual(x.ConvertToArabic('VIII'), 8)
        self.assertEqual(x.ConvertToArabic('xl'), 40)
        self.assertEqual(x.ConvertToArabic('CD'), 400)
        self.assertEqual(x.ConvertToArabic('xCviii'), 98)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()