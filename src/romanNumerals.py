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
        
    def letterToNumber(self, letter):
        if letter == 'M':
            return 1000
        elif letter == 'D':
            return 500
        elif letter == 'C':
            return 100
        elif letter == 'L':
            return 50
        elif letter == 'X':
            return 10
        elif letter == 'V':
            return 5
        elif letter == 'I':
            return 1
        else:
            return -1
            
        
    def ConvertToArabic(self, romanNumber):
        if(self.ValidateRomanNumber(romanNumber)):
            total = 0
            romanNumber = list(romanNumber)
            for i in romanNumber:
                number = self.letterToNumber(i)
                if number >= romanNumber[i+1]:
                    suma = total + number
                else:
                    suma = total - number
                    
            return total
        else:
            return "Not a valid number"