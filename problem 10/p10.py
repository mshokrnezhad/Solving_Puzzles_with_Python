"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import numpy as np
import functools

prime_numbers = np.array([2, 3, 5])
bound = 2000000

for i in range(6, bound):
    print(i)
    sqrt_i = int((i**0.5))
    filtered_prime_numbers = prime_numbers[prime_numbers <= sqrt_i]
    remainder = i % filtered_prime_numbers

    # remainder_product = np.prod(remainder)
    # remainder_product = functools.reduce(lambda x, y: x*y, remainder)
    # if remainder_product != 0:
    #     prime_numbers = np.append(prime_numbers, i)

    flag = True
    for j in range(len(remainder)):
        if remainder[j] == 0:
            flag = False
            break
    if flag:
        prime_numbers = np.append(prime_numbers, i)

# print(prime_numbers)
print(len(prime_numbers))  # 148933
print(np.sum(prime_numbers))  # 142913828922
