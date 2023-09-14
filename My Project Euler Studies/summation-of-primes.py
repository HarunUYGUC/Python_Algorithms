"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

sum = 0

for i in range(2, 10): # It's very slow after 10000.
    flag = True

    for j in range(2, i//2 + 1):
        if (i % j == 0):
            flag = False
            break
    
    if (flag == True):
        sum += i

print(f"Sum: {sum}")


""" My code runs very slowly. So I used the following code I found online. 
I both learned something new and solved the question. :) """

def sumPrimes(n):
    sum, sieve = 0, ([True] * n)

    for p in range(2, n):
        if sieve[p]:
            sum += p

            for i in range(p*p, n, p):
                sieve[i] = False
    
    return sum

print(sumPrimes(2000000))
