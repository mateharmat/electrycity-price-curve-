'''
Created on 2017. dec. 11.

@author: User
'''
from root import Root
import xlwings as xw
import lib.readwrite as erw
import numpy
import math
import scipy.optimize as optimization
from  scipy.optimize import  differential_evolution, basinhopping
import random
import matplotlib.pyplot as plt
import lib.predplot as predplot
import statsmodels.tsa.stattools as ts
import scipy.stats
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn
import json
import lib.calc as calc
import lib.pred as pred
import lib.plothelper as pth
import lib.kalibration as kal
import lib.randopt as randopt
from lib.eh import Egyutthatok as Eh

def main(*args): 
    # EXCEL
    if len(args) == 0:
        wb = xw.Book.caller()
    # ECLIPSE
    elif len(args) == 1:
        filename = args[0][0]
        wb = xw.Book(Root.resources() + filename)
        
    df = erw.data_reader(wb)
#############   
    n = 1096  
    days = [i for i in range(len(df))]  
    price = numpy.array(df.Price)  
    holiday = numpy.array(df.Holiday)  
    lnPrice = numpy.log(price[:n])   
    
    dim = len(df)
#################     
    def func(t, alpha, beta, gamma, tau):
        return alpha + beta * holiday[int(t)] + gamma * numpy.cos((tau + t) * (2 * math.pi) / 365)
       
       
    def funcSqSum(params):
        alpha, beta, gamma, tau = params 
        return sum([(lnPrice[t] - func(t, alpha, beta, gamma, tau)) ** 2 for t in range(0, n)])
       
    x0 = [ 1.0, 1.0, 2.0, 3.0 ]

    eh=Eh()
    eh.lnPricetransp = lnPrice.reshape((len(lnPrice), 1))  
    eh.simulated=randopt.randopt(funcSqSum)[0]
    eh.value=randopt.randopt(funcSqSum)[1]
    ###############GLOBAL OPTIM
    
    f1=open('basopt.txt','r+')
    if list(f1)==[]:
        basopt = basinhopping(funcSqSum, x0)
        basopteha=basopt.x
        alpha= basopteha[0]
        beta = basopteha[1]
        gamma = basopteha[2]  
        tau = basopteha[3]
        x=[alpha,beta,gamma,tau]
        json.dump(x,f1)
    else:
        f1=open('basopt.txt','r')
        basopteha=json.load(f1)
        alpha = basopteha[0]
        beta = basopteha[1]
        gamma = basopteha[2]  
        tau = basopteha[3]
        
    f2=open('deopt.txt','r+')
    if list(f2)==[]:
        bounds = [(-1000, 1000), (-1000, 1000), (-1000, 1000), (0, 365)]
        deopt = differential_evolution(funcSqSum, bounds)
        deopteha=deopt.x
        alpha2 = deopteha[0]
        beta2 = deopteha[1]
        gamma2 =deopteha[2]  
        tau2 = deopteha[3]
        y=[alpha2,beta2,gamma2,tau2]
        json.dump(y,f2)
    else:
        f2=open('deopt.txt','r')
        deopteha=json.load(f2)
        alpha2 = deopteha[0]
        beta2 = deopteha[1]
        gamma2 =deopteha[2]  
        tau2 = deopteha[3]        


#######################Season, S_t
    season = numpy.zeros(dim) 
    for t in days:
        season[t] = func(t, alpha, beta, gamma, tau)
    S = lnPrice[:n] - season[:n]
    
#######################
    eh.deopteha=deopteha
    eh.basopteha=basopteha
    eh.deoptfv=funcSqSum(deopteha)
    eh.basoptfv=funcSqSum(basopteha)
    eh.seasonexcel=season.reshape(len(season), 1)
    eh.Swrite=S.reshape(len(S), 1)

    kalk=calc.parameters(S, n)
    Delta=kalk[6]
    Kappa=kalk[8]
    Sigma=kalk[9] 
    tol = 50  
    #####################################KALIBRATION
    kal1=kal.kalibr(S, Kappa, Sigma, Delta, tol, n, season)
    S_kal1=kal1[0]
    Pt_kal1=kal1[1]
    
    pt1=pth.plothelper(n, tol, price, Pt_kal1)   
    pthelpkal1=pt1
    
    eh.S_kalresult=S_kal1.reshape(len(S_kal1), 1)
    eh.Pt_kalresult=Pt_kal1.reshape(len(Pt_kal1), 1)
     
    
    erw.result_writer(wb,eh)
    
    kal2=kal.kalibr(S, Kappa, Sigma, Delta, tol, n, season)
    S_kal2=kal2[0]
    Pt_kal2=kal2[1]
    pt2=pth.plothelper(n, tol, price, Pt_kal2)
    pthelpkal2=pt2


    kal3=kal.kalibr(S, Kappa, Sigma, Delta, tol, n, season)
    S_kal3=kal3[0]
    Pt_kal3=kal3[1]
    pt3=pth.plothelper(n, tol, price, Pt_kal3)   
    pthelpkal3=pt3

    kal4=kal.kalibr(S, Kappa, Sigma, Delta, tol, n, season)
    S_kal4=kal4[0]
    Pt_kal4=kal4[1]
    pt4=pth.plothelper(n, tol, price, Pt_kal4)   
    pthelpkal4=pt4
         
    kal5=kal.kalibr(S, Kappa, Sigma, Delta, tol, n, season)
    S_kal5=kal5[0]
    Pt_kal5=kal5[1]
    pt5=pth.plothelper(n, tol, price, Pt_kal5)   
    pthelpkal5=pt5
    
      
############## MEAN REVERTING TEST

    print ts.adfuller(S)  #ADFULLER TEST  
    #####Hurts, mean reverting <=> H<0.5
    def hurst(ts):
        """Returns the Hurst Exponent of the time series vector ts"""
        lags = range(2, 100)
        tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]
        poly = polyfit(log(lags), log(tau), 1)
        return poly[0]*2.0
    print "Hurst(S):  %s" % hurst(S)    

   
#############################Prediction, 7 day
    tol=n
    pu = scipy.stats.norm.ppf(0.975)  #up/felso
    p = 0.0  # standard norm=0
    pd = scipy.stats.norm.ppf(0.025)  #down/also
    
    Delta=1.0
    S_pred=pred.pred(p, S, Kappa, Delta, Sigma, tol,season)[0]
    Pt_pred=pred.pred(p, S, Kappa, Delta, Sigma, tol,season)[1]
        
    S_pu=pred.pred(pu, S, Kappa, Delta, Sigma, tol,season)[0]
    Pt_pu=pred.pred(pu, S, Kappa, Delta, Sigma, tol,season)[1]
    
    S_pd=pred.pred(pd, S, Kappa, Delta, Sigma, tol,season)[0]
    Pt_pd=pred.pred(pd, S, Kappa, Delta, Sigma, tol,season)[1]
    plothelper2=predplot.prdplt(n, tol, price, Pt_pu)
    plothelper3=predplot.prdplt(n, tol, price, Pt_pd)
    plotgood=predplot.prdplt(n, tol, price, Pt_pred)

############PLOTS
    plt.figure(1)
    plt.plot(price, label='1')
    plt.plot(pthelpkal1, label='2')
    plt.title("Ar")
    plt.xlabel('Ido, napokban')
    plt.ylabel('Eur/MWh')
    # szotchasztikus folyamat
    plt.figure(2)
    plt.plot(S, label='1')
    plt.plot(S_kal1, label='2')
    plt.title("S folyamat")
    plt.xlabel('Id , napokban')
    #szezon fv plot
    plt.figure(3)
    plt.plot(season)  
    plt.title("Szezon fuggveny")
    plt.xlabel('Ido, napokban')
    #predikcio
    plt.figure(4)
    plt.plot(plothelper2[n-15:],label='pt_upper')
    plt.plot(plothelper3[n-15:], label='pt_lower')
    plt.plot(plotgood[n-15:], label='pt_pontos')
    plt.plot(price[n-15:n],label='eredeti')
    plt.title("Ar predikcio")
    plt.xlabel('Ido, napokban')
    plt.ylabel('Eur/MWh')
    #tobb kalibracio
    plt.figure(5)
    plt.plot(pthelpkal1[0:100], label='Kalibracio 1')
    plt.plot(pthelpkal2[0:100], label='Kalibracio 2')
    plt.plot(pthelpkal3[0:100], label='Kalibracio 3')
    plt.plot(price[0:50], label='Eredeti ar', linewidth=3.0)
    plt.title("Szcenariok")
    plt.xlabel('Ido, napokban')
    plt.ylabel('Eur/MWh')
    #megtobb
    plt.figure(6)
    plt.plot(pthelpkal1[0:100], label='Kalibracio 1')
    plt.plot(pthelpkal2[0:100], label='Kalibracio 2')
    plt.plot(pthelpkal3[0:100], label='Kalibracio 3')
    plt.plot(pthelpkal4[0:100], label='Kalibracio 4')
    plt.plot(pthelpkal5[0:100], label='Kalibracio 5')
    plt.plot(price[0:50], label='Eredeti ar', linewidth=3.0)
    plt.title("Szcenariok")
    plt.xlabel('Ido, napokban')
    plt.ylabel('Eur/MWh')
    plt.show()
    print'END'
    
if __name__ == '__main__':
    main(['Adatok.xlsm'])
