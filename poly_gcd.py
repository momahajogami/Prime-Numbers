from  poly_divmod import *
from euclid import inverse
from numpy import poly1d
import pdb

def poly_prime_gcd(f,g,p):
    """
    Algorithm 2.2.1 (gcd for polynomials), p. 90
    from Crandall and Pomerance,
    Prime Numbers, A Computational Perspective.

    For given polynomials f(x),
    g(x) in F[x], not both zero, this algorithm
    returns d(x) = gcd(f(x),g(x)
    """


    # 1. [initialize]

    zero = poly1d([0])
    if f.order < g.order or f == zero:
        f,g = g,f

        
    # 2. [Euclid loop]

    while g != zero:
        f,g = g, poly_prime_mod(f,g,p)

        
    # 3. [Make Monic]
    # take the leading coefficient.
    flc = f.c[0]
    
    # invert it.
    c = inverse(flc,p)
    
    # and multiply with f.
    return reduce_prime_poly(f*c,p)

