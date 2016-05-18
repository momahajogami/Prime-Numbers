import unittest
from practical_sieve import *
from random import choice, shuffle
import copy
from numpy.random import poisson 
from practical_sieve import primes_under_100 as ppp

from simple_factor import simple_factor




class testSimpleFactor(unittest.TestCase):
    def unfactor(self, pairs):
        product = 1
        for (p,e) in pairs:
            product = product * p**e
        return product

    def setUp(self):
        # produce a dictionary of numbers n
        # and their factorizations
        # d[n] = [(p1,e1),(p2,e2)...(pk,ek)]
        # where p1..pk are the distinct prime
        # factors of n in order    

        # for example:
        # d[12] = [(2,2),(3,1)]
        
        # j is the number of examples to generate
        j = 50

        # d is a dictionary 
        self.d = {}

        # pp is the average number of disctinct prime factors
        pp = 5

        # ee is the average exponent 
        ee = 5
        
        for i in range(j):
            p = poisson(pp)
            shuffled_primes = copy.deepcopy(ppp)
            shuffle(shuffled_primes)
            factors = shuffled_primes[:pp]
            factors.sort()
            pairs = []
            for factor in factors:
                # make sure e != 0
                e = poisson(ee) + 1 
                pairs.append((factor,e))
            n = self.unfactor(pairs)
            self.d[n] = pairs

    def tearDown(self):
        pass


    def test_check_dict(self):
        for n in self.d.keys():
            self.assertEqual(self.d[n], simple_factor(n))

if __name__ == '__main__':
    unittest.main()




