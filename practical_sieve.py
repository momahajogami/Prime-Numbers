def primes_in_block(small_primes, L, R, B): 
    # Algorithm 3.2.1 in Prime Numbers, A Computational Perspective.
    # p. 122
    # 0.  Choose R>L even,
    #            L > P := int_sqrt(R),
    #            B|R-L

    primes_in_range = []

    # 1. Initialize offsets.
    primes_with_offsets = []
    for p in small_primes:
        q = -(L+1+p)/2 %p
        primes_with_offsets.append((p,q))


    # 2. Process Blocks
    T = L
    while (T < R):
        block = [1]*B
        next_pwo = []
        for (p,q) in primes_with_offsets:
            j = q
            while j<B:
                block[j] = 0
                j = j + p
            # This is the way to move the offset over one block:
            q = (q-B)%p 
            next_pwo.append((p,q))
        for j in range(B):
            if block[j] == 1:
                primes_in_range.append(T + 2*j + 1)
        T = T+2*B
        primes_with_offsets = next_pwo
    return(primes_in_range)
