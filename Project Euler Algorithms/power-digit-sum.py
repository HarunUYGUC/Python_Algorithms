""" https://projecteuler.net/problem=16 """

expo_result = 2**1000
list_of_expo_result = list(str(expo_result))

sum = 0

for number in list_of_expo_result:
    sum += int(number)

print(f"Sum: {sum}")
