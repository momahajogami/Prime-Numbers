import unittest
from irreducibility_1 import *
from numpy import poly1d
from practical_sieve import odd_p_under_100 as ppp

class testIrreducibility1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    # Thanks to Paul Garrett of the University
    # of Minnesota for these examples of
    # polynomials which are irreducible modulo
    # certain primes.

    # For a complete description of each
    # example, with proof, see
    # irreducible_examples.pdf in this
    # directory. 
    
    def testGarrett_1_0_3(self):
        
        # fun fact:  if p is 3 mod 4 then x^2 +
        # 1 is irreducible mod p. 

        l = [p for p in ppp if p %4 ==3]

        f = poly1d([1,0,1])
        
        for p in l:
            self.assertTrue(is_irreducible_1(f,p))

    def testGarrett_1_0_4(self):
        l = [p for p in ppp if p %3 ==2]
        f = poly1d([1,1,1])
        for p in l:
            self.assertTrue(is_irreducible_1(f,p))

    def testGarrett_1_0_5(self):
        l = [p for p in ppp if p%5 ==1 or p%5 == 4]
        f = poly1d([1,1,1,1])
        for p in l:
            self.assertTrue(is_irreducible_1(f,p))

    def testGarrett_1_0_6(self):
        l = [p for p in ppp if p%7 ==3 or p%7 == 5]
        f = poly1d([1]*7)
        for p in l:
            self.assertTrue(is_irreducible_1(f,p))


if __name__ == '__main__':
    unittest.main()




