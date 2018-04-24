'''
Created on 2018. marc. 12.

@author: User
'''
import numpy
import math
import scipy.optimize as optimization
from  scipy.optimize import  differential_evolution, basinhopping
import random

def randopt(funcSqSum,):
    simulated = numpy.zeros((10, 4))
    value = numpy.zeros((10, 1))
    for i in range(0, 5):
        x_i = [random.randint(-20, 50), random.randint(-20, 50), random.randint(-20, 50), random.randint(-20, 50)]
        optimum = optimization.minimize(funcSqSum, x_i, method='Nelder-Mead').x
        simulated[i] = optimum  
        value[i] = funcSqSum(optimum)  
    for i in range(5, 10):
        x_i = [round(random.uniform(-20, 50), 4), round(random.uniform(-20, 50), 4), round(random.uniform(-20, 50), 4), round(random.uniform(-20, 50), 4)]
        optimum = optimization.minimize(funcSqSum, x_i, method='Nelder-Mead').x
        simulated[i] = optimum
        value[i] = funcSqSum(optimum)
    return simulated,value