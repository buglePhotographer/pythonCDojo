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
        for i in romanNumber:
            if i == 'I':
                return 1
            elif i == 'V':
                return 5
            elif i == 'X':
                return 10
            elif i == 'L':
                return 50
            elif i == 'C':
                return 100
            elif i == 'D':
                return 500
            else:
                return 1000