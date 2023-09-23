""" https://projecteuler.net/problem=3 """

from math import sqrt

# A program that finds the exact divisors of the number except 1 and itself.
divisors = []
number = 600851475143
sqrt_of_number = int(sqrt(number))

for divisor in range(2, sqrt_of_number + 1):
    if (number % divisor == 0):
        divisors.append(divisor)

        if (divisor != number//divisor):
            divisors.append(number//divisor)

# A program that finds the prime divisors of a number and the largest prime divisor.
primes = []

for num in divisors:
    is_prime = True
    sqrt_of_num = int(sqrt(num))
    
    for div in range(2, sqrt_of_num + 1):
        if (num % div == 0):
            is_prime = False
            break
    
    if (is_prime == True):
        primes.append(num)

print(max(primes))




# MY OLD CODE!!!

# For the number 600851475143, this algorithm 
# is very slow but works correctly.

# In order for the program to be faster, 
# I need to learn new methods by researching on the internet.

"""
number = 13195 
list = []
flag = True

for i in range(2, number//2):
    if (number % i == 0):
        for j in range(2, i//2):
            if (i % j == 0):
                flag = False
                
                break
        if (flag == True):
            list.append(i)

print(list)
"""
