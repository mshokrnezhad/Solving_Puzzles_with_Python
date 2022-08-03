"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

bound = 1000000
palindromes = []

while bound > 1:
    flag = False
    if str(bound) == ''.join(reversed(str(bound))):
        palindromes.append(bound)
        start = math.ceil(math.sqrt(bound))
        while start < 1000 and start > 100:
            end = bound/start
            if end < 1000 and end > 100:
                if end - math.ceil(end) == 0:
                    flag = True
                    print(bound, start, end)
            start += 1
    bound -= 1
    if flag == True:
        break
