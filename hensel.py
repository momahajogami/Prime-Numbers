# todo: Algs 2.3.8, 2.3.9

# You'll need euclid.inverse
from euclid import *

from numpy import poly1d 

# def roots_mod_p(g,p):
#     """
#     Algorithm 1.3.10 (Roots of a polynomial over F_p)
#     Given a nonzero polynomial g in F_p[x], with p an odd prime, this
#     algorithm returns the set r of the roots (without multiplicity) in
#     F_p of g.  The set r is assumed global, augmented as necessary
#     during recursive calls."""
    
#     # 1. [Initial adjustments]
#     rs = []
#     x_tothe_p_minux_x = poly1d([1]+([0]*p))+poly1d([-1,0])
#     g = gcd(x_tothe_p_minux_x, g)
#     if g(0)==0:
#         rs.append(0)
#         g = g/x

#     # 2. [Call recursive procedure and return]
#     from random import choice
#     def roots(g):
#         if poly1d.order <= 2:
#         # use quadratic formula via Alg 2.3.8 or 2.3.9
#             return quadratic_roots(g,p)
#             while (h==1 or h==g):
#                 a = choice (range(0))
#                 k = poly1d([1,a]**((p-1)/2)-1)
#                 h = gcd(k,g)

        
#     rs = rs + roots(g)
#     return r

def poly_eval(f,x):
    """This function is necessary because the
    built in function evaluate with numpy
    doesn't make use of Long integers.  
    """
    cs = f.c.tolist()
    cs.reverse()
    y = 0
    x_tothe_n = 1
    for c in cs:
        y = y + c*x_tothe_n
        x_tothe_n = x_tothe_n * x
    return y

def hensel_iterate(f,p,r):
    """Algorithm 2.3.11 (Hensel lifting).  We are given a polynomial
    f(x) in Z[x], a prime p, and an integer r that satisfies f(r) ==0
    (mod p) (perhaps supplied by Algorithm 2.3.10) and f'(r) != 0 (mod
    p).  This algorithm describes how one constructs a sequence of
    integers r_0, r_1, ... such that for each i < j, r_i == r_j (mod
    p^2^j) and f(r_i) == 0 (mod p^2^i).  The description is iterative,
    that is, we give r_0 and show how to find r_{i+1} as a  function
    of an already known r_i"""

    # 1. initial term
    i = 0
    p2i = p # p**(2**i)
    rs = [r]
    ri = r

    # function newr() that gives r_{i+1} from r_i
    def newr(ri, p2i):
        fri = poly_eval(f,ri)
        x = fri/p2i # possible because ri is a zero of f mod p2i
        fpri = poly_eval(f.deriv(1),ri)
        z = inverse(fpri, p2i) # r, not ri?
        y = -x*z % p2i
        nextr = ri + y*p2i % (p2i**2)
        return nextr

    while i<=10:
        ri = newr(ri, p2i)
        rs.append(ri)
        i = i+1
        p2i = p2i**2
                
    return rs



def test_solutions(f,p2i,solutions):
    print "let f = ", f
    for i, s in enumerate(solutions):
        fs = poly_eval(f,s)
        print i, ": f (",s,") (mod ", p2i,") == ", fs%p2i
        # fprimes = poly_eval(f.deriv(1),s)
        # print  "    f'(",s,") = ", fprimes %p2i
        p2i = p2i **2
    print "mod all those high powers of seven!!"

if __name__=="__main__":
    print "hello"
    # niven example 2.6.11
    
    f = poly1d([1,1,47])
    p = long(7)
    a = long(1)
    # print "p = 7"
    # print "a = 1"
    # print hensel_iterate(f,p,a)
    # print
    # a = 5
    # print "p = 7"
    # print "a = 5"
    # print hensel_iterate(f,p,a)
    
    print
    test_solutions(f, p, hensel_iterate(f, p, a))
    a = long(5)
    print
    test_solutions(f, p, hensel_iterate(f, p, a))
