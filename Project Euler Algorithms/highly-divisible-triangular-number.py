""" https://projecteuler.net/problem=12 """

import math

# Method 1

divisors = []
i = 1
number = 0

while True:
    number += i
    sqrt_of_number = int(math.sqrt(number))

    for divisor in range(1, sqrt_of_number + 1):
        if (number % divisor == 0):
            divisors.append(divisor)

            if (divisor != number//divisor):
                divisors.append(number//divisor)
    
    number_of_divisors = len(divisors)

    if (number_of_divisors > 500):
        print(number)
        break
    else:
        divisors.clear()

    i += 1


# Method 2

i = 1
number = 0

while True:
    number += i
    number_of_divisors = 0
    sqrt_of_number = int(math.sqrt(number))

    for divisor in range(1, sqrt_of_number + 1):
        if (number % divisor == 0):
            number_of_divisors += 1

            if (divisor != number//divisor):
                number_of_divisors += 1

    if (number_of_divisors > 500):
        print(number)
        break

    i += 1
