""" https://projecteuler.net/problem=29 """

list = []

for a in range(2, 101):
    for b in range(2, 101):
        expo = a**b

        if expo not in list:
            list.append(expo)

print(len(list))
