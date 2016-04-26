from euclid import inverse
from numpy import poly1d
from collections import deque
import pdb

def reduce_prime_poly(f,p):
    # if type(f) != numpy.lib.polynomial.poly1d
    if type(f) == int:
        f = poly1d([f])

    r = deque(f.c.tolist())
    l = []
    while r:
        # take c off of the right
        c = r.popleft()
        # reduce it mod p and append it to the left.
        l.append(int(c)%p)
    # return a poly with the reduced list of coefficients. 
    return poly1d(l)

def poly_prime_divmod(f,g,p):

    """ 
    f and g are polynomials in F_p[x]
    return q,r such that 
    f = q*g + r 
    and r.order < g.order
    """
    zero = poly1d([0])
    x = poly1d([1,0])

    d = f.order - g.order
    if d < 0:
        return zero, f

    if g == zero:
        raise ZeroDivisionError ("divmod(f,0) is undefined for all f")
    # this is a case which requires some thought.
    
    if f.order == 0:
        
        flc,glc = f.c[0],g.c[0] # get leading terms
        c = poly1d([inverse(glc,p)*flc % p])
        c = reduce_prime_poly(c,p)
        return c,zero
        
            
    count = 0
    while d >= 0 and f != zero:
        flc,glc = f.c[0],g.c[0] # get leading terms

        c = poly1d([inverse(glc,p)*flc % p])
        term = c*(x**d)

        # term*g has same degree and same leading coefficient as f.
        # The following is calculated to reduce degree of f.

        f = f - term*g  
        f = reduce_prime_poly(f,p)
       
        count += term
        d = f.order - g.order

    count = reduce_prime_poly(count,p)
    return count, f

def poly_prime_mod(f,g,p):
    """ return f % g for f,g in F_p[x]
    """
    q,r = poly_prime_divmod(f,g,p)
    return r
