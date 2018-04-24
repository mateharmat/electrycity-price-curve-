'''
Created on 2018. apr. 6.

@author: User
'''
import unittest
import numpy
import math

from lib.randopt import randopt           


class randomoptTest(unittest.TestCase):
    
    def setUp(self):
        self.n=10
        self.price=[10.490313001706124, 57.93516759505243, 21.420565037402152, 55.54054034488221, 17.109117347182, 22.12499820398821, 58.518742219687375, 42.05061238003779, 56.67048406658388, 26.52265994822264]


    def testrandopt(self):
        lnprice=numpy.log(self.price)
        holiday=[1,0,0,0,0,0,1,1,0,0]
        def func(t, alpha, beta, gamma, tau):
            return alpha + beta * holiday[int(t)] + gamma * numpy.cos((tau + t) * (2 * math.pi) / 365)
        def funcSqSum(params):
            alpha, beta, gamma, tau = params 
            return sum([(lnprice[t] - func(t, alpha, beta, gamma, tau)) ** 2 for t in range(0, self.n)])
        eredmeny=randopt(funcSqSum)
        print eredmeny
       
         
                 
if __name__== '__main__':
    unittest.main()