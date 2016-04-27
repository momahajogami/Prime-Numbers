from  poly_divmod import *
from euclid import inverse
from numpy import poly1d
import pdb

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

def poly_gcd_extended(f,g,p):
    """
    Algorithm 2.2.2 (Extended gcd for polynomials)
    p. 91 from Crandall and Pomerance, 
    Prime Numbers, a Computational Perspective.

    Let F be a field.  For given polynomials,
    f(x), g(x) in F[x], not both zero, with
    either deg f(x) >= deg g(x) or g(x) == 0,
    this algorithm returns (s(x),t(x),d(x)) in
    F[x] such that d = gcd (f,g) and sf + tg =
    d.  (For ease of notation, we may drop the
    x argument). 
    """
    def rpp(f):
        return reduce_prime_poly(f,p)
    

    # 1. [initialize]

    zero = poly1d([0])
    one = poly1d([1])
    f = reduce_prime_poly(f,p)
    g = reduce_prime_poly(g,p)
    swap = False
    if f.order < g.order or f == zero:
        f,g = g,f
        swap = True

    s,t,d,u,v,w = one,zero,f,zero,one,g


        
    # 2. [Extended Euclid loop]

    while w != zero:
        q,r = poly_prime_divmod(d,w,p)
        s,t,d,u,v,w = u,v,w,rpp(s-q*u), rpp(t-q*v), r        

    
    # 3. [Make Monic]
    
    # take the leading coefficient of d.
    # invert it.
    
    c = poly1d([inverse(d.c[0],p)])
    if swap:
        s,t = t,s
    s,t,d = rpp(c*s), rpp(c*t), rpp(c*d)

    return s,t,d

