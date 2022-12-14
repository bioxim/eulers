"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    
    EXPLANATION
    
    Pythagoras
        a2 + b2 = c2

        Also we have
        a + b + c = 1000

        algebra, rearrange c to left
        c = 1000 - (a + b)

        insert c back in pythagoras
        a2 + b2 = (1000 - (a + b))2

        multiply out
        a2 + b2 = 1000000 - 2000 * (a + b) + (a + b)2

        multiply out
        a2 + b2 = 1000000 - 2000 * (a + b) + a2 + 2 * a * b + b2

        rearrange a2 + b2 to simplify
        0 = 1000000 - 2000 * (a + b) + 2 * a * b

        rearrange unknowns to left
        2000 * (a + b) - 2 * a * b = 1000000

        simplify, / 2
        1000 * (a + b) - a * b = 500000

        factorsize
        a(1000 - b) + 1000 * b = 500000

        rearrange
        a(1000 - b) = 500000 - 1000 * b

        a = (500000 - 1000 * b) / (1000 - b)
"""

def triplet(n):
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = n - a - b
            if c < 0:
                break;
            if a * a + b * b == c * c:
                return a*b*c 
    print(f"Sin resultados para {n}")