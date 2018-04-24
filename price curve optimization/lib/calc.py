'''
Created on 2017. dec. 11.

@author: User
'''
import numpy
import math
from numpy import sqrt
def parameters(S,n):
    Sx = 0
    Sxx = 0
    Sy = 0
    Syy = 0
    Sxy = 0
    for i in range(1, n):
        Sx = Sx + S[i - 1]
        Sxx = Sxx + S[i - 1] ** 2
        Sy = Sy + S[i]
        Syy = Syy + S[i] ** 2
        Sxy = Sxy + S[i] * S[i - 1]

    a = (n * Sxy - Sx * Sy) / (n * Sxx - Sx ** 2)    
    Delta = 1.0  ####t-1 ->t
    sde = sqrt((n * Syy - Sy ** 2 - a * (n * Sxy - Sx * Sy)) / (n * (n - 2)))
    Kappa = -1 * math.log(a) / Delta  
    Sigma = sde * sqrt(-2 * math.log(a) / (Delta * (1 - a ** 2)))
    return Sx,Sxx,Sy,Syy,Sxy,a,Delta,sde,Kappa,Sigma
    
