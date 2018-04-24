'''
Created on 2018. marc. 10.

@author: User
'''
import numpy 
import math
from numpy import sqrt

def pred(p,S,Kappa,Delta,Sigma,tol,season):
    S_pred = numpy.zeros(7)
    S_pred[0] = S[tol - 1] * math.exp((-Kappa * Delta)) + Sigma * sqrt((1 - math.exp((-2 * Kappa * Delta))) / (2 * Kappa)) * p
    for i in range(1, 7):  
        Delta = i
        S_pred[i] = S_pred[i - 1] * math.exp((-Kappa * Delta)) + Sigma * sqrt((1 - math.exp((-2 * Kappa * Delta))) / (2 * Kappa)) * p
    season_pred = season[tol:tol + 7]   
    lnPt_pred = season_pred + S_pred   
    Pt_pred = numpy.exp(lnPt_pred)  
    return S_pred, Pt_pred