target = 600851475143
max_prime_factor = 0

for i in range(target)[2:]:
    if target%i == 0:
        target = target/i
    if target<i:
        max_prime_factor = i
        break

print(max_prime_factor)
