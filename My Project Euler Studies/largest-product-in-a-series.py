""" https://projecteuler.net/problem=8 """

with open(r"C:\Users\Harun\Desktop\Python_Algorithms\My Project Euler Studies\largest-product-in-a-series.txt") as file:
    list_of_numbers = file.readline()
    greatest_products = []

    for digit in range(len(list_of_numbers) - 12):
        thirteen_digit = list_of_numbers[digit:(digit + 13)]
        multi = 1

        for number in thirteen_digit:
            multi *= int(number)
            greatest_products.append(multi)
        
    print(f"Answer: {max(greatest_products)}")
