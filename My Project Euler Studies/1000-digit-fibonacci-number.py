""" https://projecteuler.net/problem=25 """

a = 1
b = 1
fib_list = [a, b]
last_index = len(fib_list) - 1

while True:
    sum = a + b
    fib_list.append(sum)

    a = b
    b = sum

    last_index += 1

    if (len(str(fib_list[last_index])) == 1000):
        print(last_index + 1)
        break
