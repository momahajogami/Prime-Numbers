def legendre(a,m):
    """
    Algorithm 2.3.5 (Calculation of Legendre /
    Jacobi symbol).  p 98 from Crandall and
    Pomerance, Prime Numbers, a Computational
    Perspective. 

    Given positive odd integer m, and an
    integer a, this algorithm returns the
    Jacobi symbol (a/m), which for m an odd
    prime is also the Legendre symbol.
    """

    # 1. [Reduction loops]

    a = a%m
    t = 1
    while a != 0:
        while not (a&1):
            a = a /2
            if m%8 in [3,5]:
                t = -t
        a,m = m,a
        if a == m and a%4 == 3:
            t = -t
        a = a%m

    # 2. [Termination]
    
    if m ==1:
        return t
    return 0
