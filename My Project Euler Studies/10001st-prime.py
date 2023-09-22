""" https://projecteuler.net/problem=7 """

from math import sqrt

num = 4
num_of_primes = 2

while (num_of_primes != 10001):
    num += 1
    is_prime = True
    sqrt_of_num = int(sqrt(num))
    
    for divisor in range(2, sqrt_of_num + 1):
        if (num % divisor == 0):
            is_prime = False
            break

    if (is_prime == True):
        num_of_primes += 1

print(f"{num_of_primes}. prime: {num}")
