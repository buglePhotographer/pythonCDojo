'''
Created on Dec 8, 2014

@author: gustavo.citati
'''

class romanNumerals(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
    def ConvertToArabic(self, romanNumber):
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