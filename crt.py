import pdb
def euclid(x,y):
    """Return a,b,g such that ax + by = g = gcd(x,y)"""
    # initalize
    (a,b,g,u,v,w) = (1,0,x,0,1,y)
    while w > 0:
        q = g/w # integer division
        (a,b,g,u,v,w) = (u,v,w,a-q*u, b-q*v, g-q*w)
    return (a,b,g)

def inverse(n,m):
    a,b,g = euclid(n,m)
    # this makes sense when g is 1
    return a


def precomputation(moduli):
    r = len(moduli)
    mus = [moduli[0]]
    cs = [1]
    acc = 1
    for i in range(r)[1:]:
        acc = acc*moduli[i-1]
        c = inverse(acc, moduli[i])
        mus.append(acc)
        cs.append(c)
    M = mus[r-1]* moduli[r-1]
    return (mus, cs, M)

def reentry(ns, moduli, mus,cs, M):
    r = len(moduli)
    n = ns[0]
    for i in range(r)[1:]:
        u = ((ns[i]-n)*cs[i]) % moduli[i]
        n = n + u * mus[i]

    n = n % M
    return n
    
def crt_reconstruction(residues, moduli):
    """
    Algorithm 2.1.7 page 88
    Using the nomenclature of Theorem 2.1.6, we assume r>=2 fixed,
    pairwise co-prime moduli, a list of integers whose product we will
    compute in precomputation as M and another list of integers of the
    same length, the residues.  This algorithm returns the unique n,
    0<=n < M with the given residues.  After the precomputation step,
    the algorithm may be reentered for future evaluations of such n
    with the moduli remaining fixed. 
    """
    mus,cs, M = precomputation(moduli)
    return reentry(residues, moduli, mus,cs, M), M


if __name__ == "__main__":
    residues = [1,1,3,5,9]
    moduli = [2,3,5,7,11]
    n, m = crt_reconstruction(residues,moduli)
    print n, m 
        
             
             
