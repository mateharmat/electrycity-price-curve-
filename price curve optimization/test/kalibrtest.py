'''
Created on 2018. apr. 6.

@author: User
'''

import unittest
import numpy
import math
from lib.kalibration import kalibr        


class kalibrTest(unittest.TestCase):
    
    def setUp(self):
        self.n=10
        self.tol=3
  
        self.Kappa=0.7
        self.Sigma=2.3
        self.Delta=1.0
        self.season=[0.09633456843240229, 0.659610949581546, 0.9692609249683268, 0.24780881001043653, 0.5374683761842695, 0.10858790696079712, 0.4927248859849187, 0.8237278327031942, 0.6430358932732482, 0.4855791575987237]
       
        self.S=[0.4955444724422472, -0.18844119840104334, 0.444811538831846, 2.8434248560732542, -0.35626503864630366, 2.3458540878001415, 2.6324712689819707, 0.6693100342114127, 2.7073838041601794, 2.5390156850897947]
              
     
    def testkalibr(self):
        self.season=numpy.random.rand(13)
        k=kalibr(self.S,self.Kappa,self.Sigma,self.Delta,self.tol,self.n,self.season)
        print k
                 
if __name__== '__main__':
    unittest.main()