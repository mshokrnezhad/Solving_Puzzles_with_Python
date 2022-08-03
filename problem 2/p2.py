
fib = []
fib.append(1)
fib.append(2)
count = 0

i = 2
while fib[-1] < 4000000:
    if fib[i-2]+fib[i-1] > 4000000:
        break
    else:
        fib.append(fib[i-2]+fib[i-1])
    i += 1

for i in range(len(fib)):
    if fib[i]%2 == 0:
        count += fib[i]

print(count)
