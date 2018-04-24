'''
Created on 2018. marc. 12.

@author: User
'''
import numpy

def prdplt(n,tol,price,predikcio):
    plothelper = numpy.zeros(n + 7)
    for i in range(0, n + 7):
        if i < tol:
            plothelper[i] = price[i]
        else:
            plothelper[i] = predikcio[i - tol]
    return plothelper