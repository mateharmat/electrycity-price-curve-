'''
Created on 2018. marc. 14.

@author: User
'''

import unittest
import numpy
import math
from lib.plothelper import plothelper as pth  
from lib.kalibration import kalibr            
from lib.predplot import prdplt as pr         
from lib.pred import pred                     
from lib.calc import parameters as param      
from lib.randopt import randopt               


class functionTest(unittest.TestCase):
    
    def setUp(self):
        self.n=10
        self.tol=3
        self.price=[10.490313001706124, 57.93516759505243, 21.420565037402152, 55.54054034488221, 17.109117347182, 22.12499820398821, 58.518742219687375, 42.05061238003779, 56.67048406658388, 26.52265994822264]
        self.kalibralt=[17, 48, 45, 41, 36, 59, 22, 38, 42, 43]
        self.Kappa=0.7
        self.Sigma=2.3
        self.Delta=1.0
        self.season=[0.09633456843240229, 0.659610949581546, 0.9692609249683268, 0.24780881001043653, 0.5374683761842695, 0.10858790696079712, 0.4927248859849187, 0.8237278327031942, 0.6430358932732482, 0.4855791575987237]
        self.predikcio=[48.259960028800364, 18.174957133874564, 17.753641991959306, 48.68847317418984, 34.24439890562748, 11.976421053818338, 22.186530218315355, 12.534481312276148, 40.27261824503057, 7.205894283033469]
        self.S=[0.4955444724422472, -0.18844119840104334, 0.444811538831846, 2.8434248560732542, -0.35626503864630366, 2.3458540878001415, 2.6324712689819707, 0.6693100342114127, 2.7073838041601794, 2.5390156850897947]
        self.p=0.89
        
     
    def testpthelp(self):
        rst=pth(self.n, self.tol, self.price, self.kalibralt)
        print rst
        mo=[10.490313001706124, 57.93516759505243, 21.420565037402152, 17.0, 48.0, 45.0, 41.0, 36.0, 59.0, 22.0]
        self.assertEqual(rst.tolist(), mo)
     
    def testpredplot(self):
        self.tol=self.n
        res=pr(self.n,self.tol,self.price,self.predikcio)
        print res
        mo=[10.490313001706124, 57.93516759505243, 21.420565037402152, 55.54054034488221, 17.109117347182, 22.12499820398821, 58.518742219687375, 42.05061238003779, 56.67048406658388, 26.52265994822264, 48.259960028800364, 18.174957133874564, 17.753641991959306, 48.68847317418984, 34.24439890562748, 11.976421053818338, 22.186530218315355] 
        self.assertEquals(res.tolist(), mo)
     
    def testkalibr(self):
        self.season=numpy.random.rand(13)
        k=kalibr(self.S,self.Kappa,self.Sigma,self.Delta,self.tol,self.n,self.season)
        print k
     
    def testpred(self):
        predres=pred(self.p, self.S, self.Kappa, self.Delta, self.Sigma, self.tol, self.season)
        print predres
        mo1=[1.7225326803229772, 2.3570302215310575, 2.2578406597937235, 1.993497461132033, 1.8480537933194625, 1.7850481765832051, 1.7566040618594976]
        mo2=[7.17312562320556, 18.07443660507491, 10.659255403865386, 12.015798758860786, 14.465718748911588, 11.337140090145114, 9.413861393796243]
        self.assertEqual(predres[0].tolist(), mo1) 
        self.assertEqual(predres[1].tolist(), mo2)
        
    def testcalc(self):
        resparam=param(self.S,self.n)
        print resparam
        mo=(11.594093825453708, 28.901760772586808, 13.63756503810125, 35.10279709755074, 15.862329721976355, 0.0032865871779026628,1.0, 1.436328309133792, 5.717905584550484, 4.8572398965292445)
        self.assertEqual(resparam, mo)
     
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