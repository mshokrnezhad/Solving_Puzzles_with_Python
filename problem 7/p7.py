"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

prime_numbers = [2]
target_length = 10001
count = 3


def IsPrime(number, prime_numbers):
    for i in prime_numbers:
        if(number % i == 0):
            return False
    else:
        return True


while(len(prime_numbers) < target_length):
    if(IsPrime(count, prime_numbers)):
        prime_numbers.append(count)
    count += 1

print(len(prime_numbers), prime_numbers[-1])
