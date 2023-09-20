"""
https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1. 

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the 
sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

# Method 1

fact = 1

for i in range(1, 101):
    fact *= i

fact = str(fact)
sum = 0

for number in fact:
    sum += int(number)

print(sum)


# Method 2

def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact *= i
    
    return fact

def sum_of_digits(fact):
    fact = str(fact)
    sum = 0

    for number in fact:
        sum += int(number)

    return sum

print(sum_of_digits(factorial(100)))


# Method 3

def sum_of_digits(func, num):
    fact = str(func(num))
    sum = 0

    for number in fact:
        sum += int(number)

    return sum

print(sum_of_digits(factorial, 100))
