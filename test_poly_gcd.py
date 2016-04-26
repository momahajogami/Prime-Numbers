import unittest
import pdb
from random import choice
from poly_divmod import *
from poly_gcd import *
from numpy import poly1d

class testPolyPrimeGcd(unittest.TestCase):
    def random_p_poly(self,degree,p):
        cs = []
        from random import choice
        residues = range(p)
        cs = [choice(residues) for term in range(degree+1)]
        return (poly1d(cs))

    def setUp(self):
        from practical_sieve import primes_under_100 as ppp
        self.cases = []

        # smaller primes for more likelyhood of nontrivial gcd
        
        ppp = ppp[7:15]
        
        # the range of degrees
        
        rd = range(11)
       
        # generate this many polynomials:
        
        for i in range(8):  
            p = choice(ppp)
            # choose random degree for f.
            df,dg = choice(rd), choice(rd)
            f,g = self.random_p_poly(df,p),self.random_p_poly(dg,p)
            self.cases.append((f,g,p))

    def tearDown(self):
        del self.cases

    def printReport(self,f,g,d,p,i):
        print 
        print '#'*8
        print "test #", i
        print '#'*8
        print
        print "f = "
        print f
        print "g = "
        print g
        print "d = "
        print d
        print "p = ",p

        
    def test_f_g_pairs(self):

        # choose 0 to use fresh, random polynomials.
        #        1 to load from file
        
        switch = 1
        if switch==0:
            
            # you can choose the list of random
            # cases which were determined in
            # self.setup():
            
            polynomials = self.cases
        else:
            
            # or you could load a static collection
            # of random cases from a file:
            
            from pickle import load
            f = open('pickle_test_poly_gcd','r')
            polynomials = load(f)
    
        one = poly1d([1])
        for i,(f,g,p) in enumerate(polynomials):

            # here is what is being tested
            d = poly_prime_gcd(f,g,p)

            self.printReport(f,g,d,p,i)

            # to check that this is indeed the gcd,
            # first compute div and mod of f and g with d.
            
            qf,rf = poly_prime_divmod(f,d,p)
            qg,rg = poly_prime_divmod(g,d,p)


            # then test that the remainder is zero.
            
            zero = poly1d([0])
            self.assertEqual(rf,zero)
            self.assertEqual(rg,zero)

            # and that d doesn't divide the quotient.
            # rqf is the remainder after dividing qf by d.
            # rqg is the remainder after dividing qf by d.
            
            qqf,rqf = poly_prime_divmod(qf,d,p)
            qqg,rqg = poly_prime_divmod(qg,d,p)

            self.assertTrue(rqf != zero or d == one)
            self.assertTrue(rqg != zero or d == one)
            
    
if __name__ == '__main__':
    unittest.main()





    

# def test_from_book(self):
#     f = poly1d([7, 0, 1, 0,0,0,0,0,0, 7, 0, 1])
#     g = poly1d([-7,0, -1,0,0,7, 0, 1])
#     q,r = poly_prime_divmod(f,g,13)
#     h =
#     k = 
#     self.assertEqual(q,h)
#     self.assertEqual(r,k)
