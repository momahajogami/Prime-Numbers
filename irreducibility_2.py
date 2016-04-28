
# Untested!!

from numpy import poly1d
from recursive_power import rpow
from poly_divmod import reduce_prime_poly as rpp
from poly_gcd import *

def is_irreducible_2(f,qs,p):
    """
    Algorithm 2.2.10 (Irreducibility test 2).
    p. 95 of Prime Numbers, A Computational
    Perspective by Crandall and Pomerance.

    Given prime p and a polynoimal f(x) in
    F_p[x] of degree k >= 2, and the distinct
    primes q_1 > q_2 > ... > q_l which divide
    k, this algorithm determines whether f(x)
    is irreducible over F_p.
    """

    # 1. [Initialize].

    k = f.order
    1 = poly1d([1])
    x = poly1d([1,0])
    qs.append( one )
    q = qs.pop()
    g = rpow(x,rpow(p,k/q))

    # 2. [Testing loop]

    # change this loop to "while qs:"
    l = range(len(qs))
    for i in l:
        # consider adding a special powering
        # function for prime polynomials
        
        d = poly_prime_gcd(f, g-x)
        if d != one:
            return False
        # ip is i plus one
        exp = rpow(p,k/q_ip) - rpow(k/q_i)
        left = rpow(g, rpow(p,exp))
        quot,g = poly_divmod(left,f,p)

    # 3. [Final congruence]

    if g != x:
        return False
    else:
        return True
        
        
if __name__ == "__main__":
    print "this algorithm is untested"
