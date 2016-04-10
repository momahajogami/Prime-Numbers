import random
rows = []
for i in range(3): 
    row = []
    for i in range(3+1):
        a = random.choice(range(7))
        row.append(a)
    rows.append(row)

print rows

def euclid(x,y):
    """Return a,b,g such that ax + by = g = gcd(x,y)"""
    # initalize
    (a,b,g,u,v,w) = (1,0,x,0,1,y)
    while w > 0:
        q = g/w # integer division
        (a,b,g,u,v,w) = (u,v,w,a-q*u, b-q*v, g-q*w)
    return (a,b,g)


