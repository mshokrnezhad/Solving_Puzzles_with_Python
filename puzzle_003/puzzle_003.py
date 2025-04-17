"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

target = 600851475143
max_prime_factor = 0

for i in range(target)[2:]:
    if target % i == 0:
        target = target/i
    if target < i:
        max_prime_factor = i
        break

print(max_prime_factor)
