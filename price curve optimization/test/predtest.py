'''
Created on 2018. apr. 6.

@author: User
'''

import unittest
import numpy
import math
from lib.pred import pred                   


class predikcioTest(unittest.TestCase):
    
    def setUp(self):
        self.tol=3
        self.Kappa=0.7
        self.Sigma=2.3
        self.Delta=1.0
        self.season=[0.09633456843240229, 0.659610949581546, 0.9692609249683268, 0.24780881001043653, 0.5374683761842695, 0.10858790696079712, 0.4927248859849187, 0.8237278327031942, 0.6430358932732482, 0.4855791575987237]
        self.S=[0.4955444724422472, -0.18844119840104334, 0.444811538831846, 2.8434248560732542, -0.35626503864630366, 2.3458540878001415, 2.6324712689819707, 0.6693100342114127, 2.7073838041601794, 2.5390156850897947]
        self.p=0.89
        

    def testpred(self):
        predres=pred(self.p, self.S, self.Kappa, self.Delta, self.Sigma, self.tol, self.season)
        print predres
        mo1=[1.7225326803229772, 2.3570302215310575, 2.2578406597937235, 1.993497461132033, 1.8480537933194625, 1.7850481765832051, 1.7566040618594976]
        mo2=[7.17312562320556, 18.07443660507491, 10.659255403865386, 12.015798758860786, 14.465718748911588, 11.337140090145114, 9.413861393796243]
        self.assertEqual(predres[0].tolist(), mo1) 
        self.assertEqual(predres[1].tolist(), mo2)
  
                 
if __name__== '__main__':
    unittest.main()