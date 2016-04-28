
from numpy import poly1d
from recursive_power import *
from poly_divmod import reduce_prime_poly as rpp
from poly_divmod import poly_prime_mod as ppmod
from poly_gcd import *
import pdb

def is_irreducible_1(f,p):
    """
    Algorithm 2.2.9 (Irreducibility test 1).
    Given prime p and a polynoimal f(x) in
    F_p[x] of degree k >= 2, this algorithm
    determines whether f(x) is irreducible over
    F_p.
    """

    # 1. [Initialize].

    one = poly1d([1])
    x = poly1d([1,0])
    g = x

    # 2. [Testing loop]

    # Use integer division.
    
    l = range(f.order/2)
    for i in l:

        # reminder:
        # rpppow for "Recursive Prime Poly POWer"
        # ppmod for "Prime Power MOD"
        
        g = ppmod(rpppow(g,p,p),f,p)
        d = poly_prime_gcd(f, g-x,p)
        if d != one:
            return False
    return True
        
        
if __name__ == "__main__":
    print "this algorithm is untested"
