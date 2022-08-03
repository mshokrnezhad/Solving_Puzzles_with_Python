"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np

limit = 20 + 1
min_divisible_to_limit = 1
counts = np.zeros(limit)
counts[1] = 1
counts[2] = 1
primal_nums = [2, 3, 5, 7, 11, 13, 17, 19]


def find_factors(counts_temp, num):
    if num in primal_nums:
        counts_temp[num] += 1
    else:
        for j in range(2, num):
            if num % j == 0:
                counts_temp[j] += 1
                find_factors(counts_temp, int(num/j))
                break
    return counts_temp


for i in range(3, limit):
    counts_temp = np.zeros(limit)
    counts_temp = find_factors(counts_temp, i)
    for j in range(len(counts)):
        if counts[j] < counts_temp[j]:
            counts[j] = counts_temp[j]

for i in range(0, len(counts)-1):
    min_divisible_to_limit *= i**counts[i]

print(counts[1:])
print(int(min_divisible_to_limit))
