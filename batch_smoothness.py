from copy import deepcopy
def euclid(x,y):
    """Return a,b,g such that ax + by = g = gcd(x,y)"""
    # initalize
    (a,b,g,u,v,w) = (1,0,x,0,1,y)
    while w > 0:
        q = g/w # integer division
        (a,b,g,u,v,w) = (u,v,w,a-q*u, b-q*v, g-q*w)
    return (a,b,g)



def bernstein_test(primes, numbers):
    """Algorithm 3.3.1  p. 130"""

    class Tree(object):
        def __init__(self):
            self.left = None
            self.right = None
            self.data = None
        def __str__(self):
            l = self.left.__repr__()
            c = self.data.__repr__()
            r = self.right.__repr__()
            lparen = '('
            rparen = ')'
            comma = ','
            return lparen + l + comma + c + comma + r + rparen

        def __repr__(self):
            l = self.left.__repr__()
            c = self.data.__repr__()
            r = self.right.__repr__()
            lparen = '('
            rparen = ')'
            comma = ','
            return lparen + l + comma + c + comma + r + rparen

    # compute M for step 3
    M = max(numbers)
    numcopy = deepcopy(numbers) # since numbers is destroyed in step 2
                      # but needed in step 3
    
    # Step 1. [Compute product trees]
    # Step 1. a. Compute the product tree for P
    trees = []
    # assemble a list of baby trees
    # each tree is a pair of primes and their product. 
    while primes:

        t = Tree()
        # pop returns the zeroth element and removes it, shortening the list
        t.left = primes.pop(0)
        if primes:
            t.right = primes.pop(0)
        if not t.right:
            t.data = t.left
        else:
            t.data = t.left * t.right
        trees.append(t)
        
    while len(trees) > 1:
        next_trees = []
        while trees:
            t = Tree()
            t.left = trees.pop(0)
            if trees:
                t.right = trees.pop(0)
            if not t.right:
                t.data = t.left.data
            else:
                t.data = t.left.data * t.right.data
            next_trees.append(t)

        trees = next_trees
    pt = trees.pop(0)

    # Step 1. b. Set P as the product for members of P
    P = t.data


    # Step 1. c. Compute the product tree T for X, but only for products at most P;
    # Note that I use zeroes where the text uses asterisks.
    # This is okay, I thought about it. 
    trees = []
    # assemble a list of baby trees
    # each tree is a pair of primes and their product. 
    while numbers:

        t = Tree()
        # pop returns the zeroth element and removes it, shortening the list
        t.left = numbers.pop(0)
        if numbers:
            t.right = numbers.pop(0)
        if not t.right:
            t.data = t.left
        else: # both t.right and t.left exist (are not None)
            d = t.left * t.right
            if d < P:
                t.data = d
            else:
                t.data = 0
        trees.append(t)
        
    while len(trees) > 1:
        next_trees = []
        while trees:
            t = Tree()
            t.left = trees.pop(0)
            if trees:
                t.right = trees.pop(0)
            if not t.right:
                t.data = t.left.data
            else:
                d = t.left.data * t.right.data
                if d < P:
                    t.data = d
                else:
                    t.data = 0
            next_trees.append(t)
        trees = next_trees
    nt = trees.pop(0)

    # Step 2. [Compute the remainder tree]
    def compute_remainder_tree(t,P):
        # Let each zero entry be P
        # Otherwise, replace each entry T with T mod P
        rt = Tree()

        # center
        T = t.data
        if T == 0:
            rt.data = P
        else:
            rt.data = P % T

        # left 
        if isinstance(t.left,Tree):
            # this right here is sort of the whole point of the algorithm. 
            rt.left = compute_remainder_tree(t.left,rt.data)
        else:
            rt.left = P% t.left 

        # right
        if isinstance(t.right,Tree):
            rt.right = compute_remainder_tree(t.right,rt.data)
        else:
            if not t.right:
                rt.right = None
            else:
                rt.right = P% t.right 

        return rt
    rt = compute_remainder_tree(nt,P)
    
    # Step 3. [Find smooth parts]
    numbers = numcopy
    
    e = 1
    f = 2
    while M < f:
        f = f**2
        e = e+1


    def listFromTree(t):
        s = Tree()

        # left
        if isinstance(t.left,Tree):
            l = listFromTree(t.left)
        else:
            l = [t.left]

        # right
        if isinstance(t.right,Tree):
            r = listFromTree(t.right)
        else:
            r = [t.right]

        return l +  r
    remainders = listFromTree(rt)
    
    gcds = []
    numbers = numcopy
    print "numbers: ",numbers
    print "remainders: ",remainders
    while numbers:
        (r,x) = remainders.pop(0), numbers.pop(0)
        s = r**2
        for i in range(e):
            s = s**2
        a,b,g = euclid (s,x) # throw away a and b
        gcds.append((x,g))

    return (pt,nt,rt, gcds)



if __name__ == "__main__":
    # The example from page 129
    (pt,nt,rt,gcds) =  bernstein_test([2,3,5,7,11,13,17,19],range(1001,1009))

    print
    print "Example from page 129."
    print 
    print "Product tree for P = {2,3,5,7,11,13,17,19}:"
    print pt
    print
    print "Product tree for X = {1001,1002,...,1008}:"
    print nt
    print
    print
    print "Remainder tree P mod T"
    print rt
    print
    print
    print "[(x,g)] where g is the largest divisor of x composed of primes from P"
    print gcds
    print
    print


