""" https://projecteuler.net/problem=35 """
# It hasn't been done yet.

from math import sqrt

primes = []

for num in range(2, 100):
    is_prime = True
    sqrt_of_num = int(sqrt(num))
    
    for divisor in range(2, sqrt_of_num + 1):
        if (num % divisor == 0):
            is_prime = False
            break

    if (is_prime == True):
        primes.append(str(num))

all_rotations_prime = []

for prime in primes:
    if prime[1::-1] in primes:
        all_rotations_prime.append(prime)

    # It is quite difficult to do this up to 1 million by trying one by one.

    # if (len(prime) == 1):
    #     all_rotations_prime.append(prime)
    # elif (len(prime) == 2):
    #     if prime[1::-1] in primes:
    #         all_rotations_prime.append(prime)
    # elif (len(prime) == 3):
    #     new_number1 = prime[2] + prime[1] + prime[0]

    #     if prime[2:-1] and new_number1 in primes:
    #         all_rotations_prime.append(prime)

print(len(all_rotations_prime))
