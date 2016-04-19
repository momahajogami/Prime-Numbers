import unittest
from random import choice
from poly_divmod import *
from numpy import poly1d

class testPolyPrimeDivmod(unittest.TestCase):
    def random_p_poly(self,d,p):
        cs = []
        from random import choice
        residues = range(p)
        cs = [choice(residues) for term in range(d+1)]
        return (poly1d(cs))

    def setUp(self):
        from practical_sieve import primes_under_10000 as ppp
        self.cases = []
        
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
        
    def test_f_g_pairs(self):
        for i,(f,g,p) in enumerate(self.cases):
            print 
            print '#'*8
            print "test #", i
            print '#'*8
            print
            print "p = ", p
            print "f = "
            print f
            print "g = "
            print g
            print "p = ",p
            (q,r) = poly_prime_divmod(f,g,p)
            print "q = "
            print q
            print "r = "
            print r
            self.assertTrue(r.order == 0 or r.order < g.order)
            h = reduce_prime_poly(g*q + r, p)
            self.assertEqual(f.order,h.order)
            self.assertEqual(f,h)

    
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
