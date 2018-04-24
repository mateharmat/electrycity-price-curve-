'''
Created on 2018. marc. 12.

@author: User
'''
import numpy
import math
from numpy import log, sqrt



def kalibr(S,Kappa,Sigma,Delta,tol,n,season):
    S_kal = numpy.zeros(n)
    S_kal[0] = S[tol + 1] * math.exp((-Kappa * Delta)) + Sigma * sqrt((1 - math.exp((-2 * Kappa * Delta))) / (2 * Kappa)) * numpy.random.standard_normal(1)
 
    for i in range(1, n):
        S_kal[i] = S_kal[i - 1] * math.exp((-Kappa * Delta)) + Sigma * sqrt((1 - math.exp((-2 * Kappa * Delta))) / (2 * Kappa)) * numpy.random.standard_normal(1)

    season_kal = season[tol:n +tol]  
    lnPt_kal = season_kal + S_kal  
    Pt_kal = numpy.exp(lnPt_kal)  
    return S_kal, Pt_kal, season_kal
