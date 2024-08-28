"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

bound = 1000

for a in range(1, 333):  # last number is 332 = ceil(1000/3)-1
    b_bound = ((bound-a)/2)-1 if (bound-a)%2 == 0 else math.floor(((bound-a)/2))
    b_bound = int(b_bound)
    for b in range(a+1, b_bound):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c, a*b*c)
