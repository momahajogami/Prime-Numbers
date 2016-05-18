from practical_sieve import primes_in_block
primes_under_100 = [2,3,5,7]+primes_in_block([3,5,7],10,100,5)


def next_ten_thousand_primes(primes): 
    L = primes[-1]+1
    R = L + 10000
    B = 1000
    return primes_in_block(primes[1:],L,R,B)

def next_primes(primes):
    """
    Square the size of your window. 
    Usually, this is too far to go.  
    If you start with just the primes under a
    hundred and run this twice, you're looking
    at checking congruence for tens of millions
    of numbers, and this might take some
    minutes already.  
    See: next_ten_thousand_primes(primes)
    """
    
    L = primes[-1] + 1

    # Choose the largest possible upper bound
    R = L*L

    # Choose an appropriate block size,
    # which is rather arbitrary.
    B = (R-L)/10

    # Now adjust R so that B|R-L
    R = L + 10*B

    return primes_in_block(primes[1:],L,R,B)


def factor_with_primes(n, primes):
    ps.reverse()
    pairs = []
    while ps and n > 1:
        p = ps.pop()
        e = 0
        while n % p == 0:
            e = e + 1
            n = n/p
        if e>0:
            pairs.append((p,e))
    return n,pairs

def simple_factor(n):
    """ 
    This is a demonstration of how to use
    Algorithm 3.2.1 as well a as a practical
    and simple way to factor numbers of modest
    size.  Of course, the near term goal will
    be to explore the modern factoring
    algorithms, but this will do as a sandbox
    for testing and playing. 
    """
    primes = [2,3,5,7]+primes_in_block([3,5,7],10,100,10)
    n, pairs = factor_with_primes(n, primes)
    if  n == 1:
        return pairs
    primes = next_primes(primes)
    n, new_pairs = factor_with_primes(n, primes)
    pairs = pairs + new_pairs
    while n>1:
        primes = next_ten_thousand_primes(primes)
        n, new_pairs = factor_with_primes(n, primes)
        pairs = pairs + new_pairs
    return pairs
        

