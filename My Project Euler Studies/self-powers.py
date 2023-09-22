""" https://projecteuler.net/problem=48 """

sum = 0

for i in range(1, 1001):
    sum += i**i

print(str(sum)[-10:])
