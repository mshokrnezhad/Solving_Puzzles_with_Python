import math

prime_nums = [2, 3, 5, 7]
target = 1000
max_prime_factor = 0
nums = range(target+1)

for i in nums[11:]:
    flag = False
    for j in range(len(prime_nums)):
        if i % prime_nums[j] == 0:
            flag = True
            break
        if j > math.sqrt(i):
            break
    if flag == False:
        prime_nums.append(i)
        if target % i == 0:
            max_prime_factor = i

print(len(prime_nums))

for i in range(10,15):
    print(i)