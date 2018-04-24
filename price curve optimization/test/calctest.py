
import unittest
import numpy
import math

from lib.calc import parameters as param    

class calcTest(unittest.TestCase):
    
    def setUp(self):
        self.n=10
        self.S=[0.4955444724422472, -0.18844119840104334, 0.444811538831846, 2.8434248560732542, -0.35626503864630366, 2.3458540878001415, 2.6324712689819707, 0.6693100342114127, 2.7073838041601794, 2.5390156850897947]
 
        
    def testcalc(self):
        resparam=param(self.S,self.n)
        print resparam
        mo=(11.594093825453708, 28.901760772586808, 13.63756503810125, 35.10279709755074, 15.862329721976355, 0.0032865871779026628,1.0, 1.436328309133792, 5.717905584550484, 4.8572398965292445)
        self.assertEqual(resparam, mo)
   
                 
if __name__== '__main__':
    unittest.main()