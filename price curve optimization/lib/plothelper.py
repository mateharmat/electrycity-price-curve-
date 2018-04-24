'''
Created on 2018. marc. 10.

@author: User
'''
import numpy

def plothelper(n,tol,price,kalibralt):
    plothelp = numpy.zeros(n)
    for i in range(0, n):
        if i < tol:
            plothelp[i] = price[i]
        else:
            plothelp[i] = kalibralt[i - tol]
    return plothelp