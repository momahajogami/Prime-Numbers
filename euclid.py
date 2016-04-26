def simple_euclid(x,y):
    """
    Algorithm 2.1.2, page 84
    Simple Euclid's Algorithm for gcd only.
    For x,y with x>=y>=0 and x>0,
    Return g = gcd(x,y)"""

    # 1. [Euclid loop]
    while y > 0:
        x,y = y, x%y
    return x

def euclid(x,y):
    """
    Algorithm 2.1.4, page 85
    Extended Euclid's Algorithm for gcd and inverse
    Return a,b,g such that ax + by = g = gcd(x,y)"""
    # initalize
    (a,b,g,u,v,w) = (1,0,x,0,1,y)
    while w > 0:
        q = g/w # integer division
        (a,b,g,u,v,w) = (u,v,w,a-q*u, b-q*v, g-q*w)
    return (a,b,g)


# return the inverse of n mod p
# (assume p is prime)
def inverse(n,p):
    # arrange that an + bp = g = 1
    # that is an == 1 (mod p)
    a,b,g = euclid(n,p)
    return a
    
