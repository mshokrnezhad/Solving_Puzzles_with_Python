import math


def update_prime_nums(prime_nums, limit):
    for i in range(prime_nums[-1], limit+1):
        print((limit, i))
        flag = False
        for j in range(len(prime_nums)):
            if i % prime_nums[j] == 0:
                flag = True
                break
            if j > math.sqrt(i):
                break
        if flag == False:
            prime_nums.append(i)
    return(prime_nums)


limit = 4
prime_nums = [2,3]
prime_nums = update_prime_nums(prime_nums, limit)
results = [3]
i = prime_nums[-1] + 1

while len(results) < 5:
    print(i)
    if i > limit:
        limit = i
        prime_nums = update_prime_nums(prime_nums, limit)
    if i in prime_nums:
        flag = False
        for j in range(len(results)):
            target = int(str(results[j])+str(i))
            if target <= limit:
                if target not in prime_nums:
                    flag = True
            else:
                limit = target
                prime_nums = update_prime_nums(prime_nums, limit)
                if target not in prime_nums:
                    flag = True
            target = int(str(i)+str(results[j]))
            if target <= limit:
                if target not in prime_nums:
                    flag = True
            else:
                limit = target
                prime_nums = update_prime_nums(prime_nums, limit)
                if target not in prime_nums:
                    flag = True
        if flag == False:
            results.append(i)
            print(i)
    i += 1

print(results)
