import unittest
import pdb
from random import choice
from poly_divmod import *
from poly_gcd_extended import *
from numpy import poly1d
from euclid import inverse

def make_monic(f,p):
    if type(f) == int:
        f = poly1d([f])
    f = reduce_prime_poly(f,p)
    r = deque(f.c.tolist())

    # multiply each term by inverse of leading coefficient

    factor = inverse(f.c[0],p)
    l = []
    while r:
        # take c off of the right
        c = r.popleft()
        # reduce it mod p and append it to the left.
        l.append(int(factor * c)%p)
    # return a monic poly
    return poly1d(l)


def poly_prime_gcd(f,g,p):
    s,t,d = poly_gcd_extended(f,g,p)
    return d

class testPolyPrimeGcdExtended(unittest.TestCase):
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
        
        rd = range(17)
       
        # generate this many polynomials:
        
        for i in range(101):  
            p = choice(ppp)
            # choose random degree for f.
            df,dg = choice(rd), choice(rd)
            f,g = self.random_p_poly(df,p),self.random_p_poly(dg,p)
            self.cases.append((f,g,p))

        # triplets of polys for testRiggedGCD:
        
        self.rigged_cases = []
        for i in range(8):  
            p = choice(ppp)
            # choose random degree for f.
            df,dg,dh = choice(rd), choice(rd), choice(rd)
            f,g = self.random_p_poly(df,p),self.random_p_poly(dg,p)
            h = self.random_p_poly(dh,p)
            self.rigged_cases.append((f,g,h,p))

        

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

    def testPage90(self):

        # from page 90 of Crandall and Pomerance

        f = poly1d([7, 0, 1, 0,0,0,0,0,0, 7, 0, 1])
        g = poly1d([-7,0, -1,0,0,7, 0, 1])

        p = 13
        d = poly_prime_gcd(f,g,p)

        h = poly1d([1,0,2])
        self.assertEqual(h,d)


        p = 7
        d = poly_prime_gcd(f,g,p)
        
        h = poly1d([1])
        self.assertEqual(h,d)


        p = 2
        d = poly_prime_gcd(f,g,p)
        
        h = poly1d([1,1,1,1])
        self.assertEqual(h,d)

        
        
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

            # uncomment below if you want a report.
            # self.printReport(f,g,d,p,i)

    def testRiggedGCD(self):

        # Now arrange for known gcd
        
        one = poly1d([1])
        polynomials = self.rigged_cases
        for i,(f,g,h,p) in enumerate(polynomials):

            # h (f,g)
            gcd_fg = poly_prime_gcd(f,g,p)
            h_gcd_fg = reduce_prime_poly(h*gcd_fg,p)
            h_gcd_fg = make_monic(h_gcd_fg,p)

            # (hf,hg)
            hf = reduce_prime_poly(h*f,p)
            hg = reduce_prime_poly(h*g,p)
            gcd_hf_hg = poly_prime_gcd(hf,hg,p)


            # the gcd of fh with gh should be h times
            # the gcd of f with g.
            # (hf,hg) = h(f,g)

            self.assertEqual(h_gcd_fg, gcd_hf_hg)

            # uncomment below if you want a report. 
            # self.printReport(hf,hg, gcd_hf_hg, p, i)

    def testExtended(self):

        # confirm that sg + th = d
        
        polynomials = self.cases
        for i,(f,g,p) in enumerate(polynomials):
            s,t,d = poly_gcd_extended(f,g,p)
            sf_plus_tg = reduce_prime_poly(s*f + t*g, p)
            self.assertTrue(sf_plus_tg == d )
        
        


if __name__ == '__main__':
    unittest.main()




