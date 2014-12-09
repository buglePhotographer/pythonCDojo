'''
Created on Dec 8, 2014

@author: gustavo.citati
'''
import re

class romanNumerals(object):
    '''
    classdocs
    '''
    
    
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def ValidateRomanNumber(self, romanNumber):
        pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        isValid = re.search(pattern, romanNumber)
        if(isValid != None):
            return True
        else:
            return False
            
        
    def ConvertToArabic(self, romanNumber):
        if(self.ValidateRomanNumber(romanNumber)):
            suma = 0
            for i in romanNumber:
                if i == 'M':
                    suma += 1000
                elif i == 'D':
                    suma += 500
                elif i == 'C':
                    suma += 100
                elif i == 'L':
                    suma += 50
                elif i == 'X':
                    suma += 10
                elif i == 'V':
                    suma += 5
                else:
                    suma += 1
                    
            return suma
        else:
            return 'Not a valid number'