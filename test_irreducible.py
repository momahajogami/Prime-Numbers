import unittest
from irreducibility_1 import *
from numpy import poly1d
from practical_sieve import odd_p_under_100 as ppp
from random import choice, shuffle
from poly_divmod import reduce_prime_poly as rpp
from pickle import dump, load
import pdb

def three_digit(n):
    """ return 3 character string 
    last 3 digits of n, padded
    with zeroes if necessary"""

    third = str(n%10)
    second = str((n%100)/10)
    first = str((n%1000)/100)
    return first + second + third

class testIrreducibility1(unittest.TestCase):
    def setUp(self):

        flag= 0
        
        # create a bunch of test cases
        if flag == 0: 
            print "entering setup"
            # fun fact:  if p is 3 mod 4 then x^2 +
            # 1 is irreducible mod p.
            data = []

            # Garrett's example 1.0.3
            l = [p for p in ppp if p %4 ==3]
            l = l[:4]
            f = poly1d([1,0,1])
            for p in l:
                d = choice(range(3))+1
                g = self.random_p_poly(d,p)
                h = rpp(f*g,p)
                data.append((f,h,p))


            # The idea for each of these blocks
            # of tests is to generate a
            # polynomial which is known to be
            # irreducible, and then another
            # which is known to be composite
            # modulo a certain prime.

            # How do we know that the
            # polynomial should be irreducible?
            # Check out the pdf included with
            # this repo.

            # Garrett's example 1.0.4
            l = [p for p in ppp if p %3 ==2]
            l = l[:4]
            f = poly1d([1,1,1])
            for p in l:
                d = choice(range(3))+1
                g = self.random_p_poly(d,p)
                h = rpp(f*g,p)
                data.append((f,h,p))

            # Garrett's example 1.0.5
            l = [p for p in ppp if p%5 ==1 or p%5 == 4]
            l = l[:4]
            f = poly1d([1,1,1,1])
            for p in l:
                d = choice(range(3))+1
                g = self.random_p_poly(d,p)
                h = rpp(f*g,p)
                data.append((f,h,p))
                
            # Garrett's example 1.0.6
            l = [p for p in ppp if p%7 ==3 or p%7 == 5]
            l = l[:4]
            f = poly1d([1]*7)
            for p in l:
                d = choice(range(3))+1
                g = self.random_p_poly(d,p)
                h = rpp(f*g,p)
                data.append((f,h,p))


            s = three_digit(choice(range(1000)))
            fname = 'data/datadump'+s
            f = open(fname,'w')
            dump(data,f)
            print "test data [(f,g,primes)] dumped in", fname
            self.data = data
        else:
            # load a bunch of test cases from file
            fname = 'data/datadump053'
            f = open(fname,'r')
            data = load(f)
            print "loading file: ", fname
            self.data = data

    def tearDown(self):
        pass


    # Thanks to Paul Garrett of the University
    # of Minnesota for these examples of
    # polynomials which are irreducible modulo
    # certain primes.

    # http://www.math.umn.edu/~garrett/

    # For a complete description of each
    # example, with proof, see
    # irreducible_examples.pdf in this
    # directory. 

    def random_p_poly(self,d,p):

        # first create a list of random residues
        cs = []
        residues = range(p)
        cs = [choice(residues) for term in range(d)]
        # add one which is not zero
        cs.append(choice(range(p-1)) + 1)
        # put it at the front
        cs.reverse()
        return (poly1d(cs))

    def testGarrett(self):
        print "running tests from http://www.math.umn.edu/~garrett/"
        print "see ./irreducible_examples.pdf"

        print_flag = True
        for (f,g,p) in self.data:
            self.assertTrue(is_irreducible_1(f,p))
            h = rpp(f*g,p)
            if is_irreducible_1(h,p):
                pdb.set_trace()
            self.assertFalse(is_irreducible_1(h,p))
            if print_flag:
                print f
                print "is irreducible  mod ",p
                print h
                print "is reducible mod ",p

        if print_flag:
            print "tested ",len(self.data)," polynomials for irreducibility."
                    


if __name__ == '__main__':
    unittest.main()




