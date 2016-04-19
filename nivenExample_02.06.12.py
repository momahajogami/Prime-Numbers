# Solve x^2 + x + 7 == 0 (mod 81)

# You'll need euclid.inverse
from euclid import *

from numpy import poly1d 


def derinverse(f,a,p): # the inverse of the derivative at a
    return inverse(f.deriv(1)(a))

if __name__=="__main__":
    print
    print "Solve x^2 + x + 7 == 0 (mod 81)"
    print 
    f = poly1d([1,1,7]) # = x^2 + x + 7
    p = 3
    solutions = [a for a in range(3) if f(a)%3 == 0]
    print "solutions = ", solutions
    # result: solutions = [1]
    a = 1
    print "The only root is a = 1"
    da = f.deriv(1)(1) % p
    print "the derivitive at a is ", da
    print "If the derivitive were not zero, Hensel's lemma "
    print "provides the existence of a unique solution "
    print "modulo p^2 and also a means of computing it."  
    print "Since the derivative here _is_ zero, we call it"
    print "a singular solution."
    print 
    print "In this case, our solution will lift to p roots modulo p^2 or not at all."
    print "In turn, each of these will lift to p roots or not at all modulo p^3."
    print
    print "f(a) % p^2 = ", f(a)%(p**2)
    print "since the root a lifts to p^2 and since f'(a) == 0 (mod p), our intelligence from Taylors' theorem tells us that f(a + tp) == 0 (mod p^2) for every t.  Indeed, we can check."
    print 
    print "[f(a + t*p) for t in range(3)]:"
    print [f(a + t*p) for t in range(3)]
    print
    print "and  [f(a + t*p)%p**2 for t in range(3)]:"
    print [f(a + t*p)%p**2 for t in range(3)]
    print 
    print "Thus is it confirmed by direct calculation "
    print "that each of the residue classes modulo p^2:"
    print 
    print "[a + t*p for t in range(3)]:"
    print [a + t*p for t in range(3)]
    print "which are congruent to a modulo p is a root of f modulo p^2." 
    print
    print "Our task is to solve this equation modulo 81 = 3^4."
    print "Next, examine each of these roots modulo p^3."
    print 
    print "[f(a + t*p)%p**3 for t in range(3)]:"
    print [f(a + t*p)%p**3 for t in range(3)]
    print 
    print "Observe that only the middle one, 4 lifts to a "
    print "root modulo 27 and recall that, by our intelligence"
    print "from Taylor's Theorem, this must lift to p roots.  "
    print "That is,"
    print "each of the p numbers 4 + p^2*t"
    print 
    print "[4 + p**2*t % p**3 for t in range(3)]:"
    print [4 + p**2*t % p**3 for t in range(3)]
    print 
    print "is a root modulo 27 as we can confirm:"
    print 
    print "[f(4 + p**2*t) % p**3 for t in range(3)]:"
    print [f(4 + p**2*t) % p**3 for t in range(3)]
    print 
    print "Now for the last round.  Evaluate f at each of"
    print 
    print "[4 + p**2*t % p**4 for t in range(3)]:"
    print [4 + p**2*t % p**4 for t in range(3)]
    print
    print "and examine f at each point for congruence "
    print " to zero modulo p^4."
    print 
    print "[f(4 + p**2*t) % p**4 for t in range(3)]:"
    print [f(4 + p**2*t) % p**4 for t in range(3)]
    print
    print "And there are no roots.  The joke's on us."
    print "We did all that work just to see that "
    print "This equation has no solution."


    

    
