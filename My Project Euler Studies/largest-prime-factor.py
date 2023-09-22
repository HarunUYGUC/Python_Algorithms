""" https://projecteuler.net/problem=3 """

from math import sqrt

divisors = []
number = 13195
sqrt_of_number = int(sqrt(number))

for divisor in range(1, sqrt_of_number + 1):
    if (number % divisor == 0):
        divisors.append(divisor)

        if (divisor != number//divisor):
            divisors.append(number//divisor)









# MY OLD CODE!!!

# For the number 600851475143, this algorithm 
# is very slow but works correctly.

# In order for the program to be faster, 
# I need to learn other methods that I researched on the internet.

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
