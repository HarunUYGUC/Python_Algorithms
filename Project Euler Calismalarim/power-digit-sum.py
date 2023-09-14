"""  
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

expo_result = 2**1000
list_of_expo_result = list(str(expo_result))

sum = 0

for number in list_of_expo_result:
    sum += int(number)

print(f"Sum: {sum}")
