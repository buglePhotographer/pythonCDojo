'''
Created on Dec 9, 2014

@author: gustavo.citati
'''

from src.romanNumerals import romanNumerals

if __name__ == '__main__':
    x = romanNumerals()
    #x.ValidateRomanNumber("XIX")
    print(x.ConvertToArabic("MDVIIIII"))