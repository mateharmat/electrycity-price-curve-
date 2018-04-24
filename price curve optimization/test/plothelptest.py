'''
Created on 2018. apr. 6.

@author: User
'''

import unittest
import numpy
import math
from lib.plothelper import plothelper as pth  

class plothelpTest(unittest.TestCase):
    
    def setUp(self):
        self.n=10
        self.tol=3
        self.price=[10.490313001706124, 57.93516759505243, 21.420565037402152, 55.54054034488221, 17.109117347182, 22.12499820398821, 58.518742219687375, 42.05061238003779, 56.67048406658388, 26.52265994822264]
        self.kalibralt=[17, 48, 45, 41, 36, 59, 22, 38, 42, 43]
        
     
    def testpthelp(self):
        rst=pth(self.n, self.tol, self.price, self.kalibralt)
        print rst
        mo=[10.490313001706124, 57.93516759505243, 21.420565037402152, 17.0, 48.0, 45.0, 41.0, 36.0, 59.0, 22.0]
        self.assertEqual(rst.tolist(), mo)
                 
if __name__== '__main__':
    unittest.main()