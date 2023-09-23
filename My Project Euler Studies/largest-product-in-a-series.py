""" https://projecteuler.net/problem=8 """

with open(r"C:\Users\Harun\Desktop\Python_Algorithms\My Project Euler Studies\largest-product-in-a-series.txt") as file:
    list_of_numbers = file.readlines()
    greatest_products = []

    for row in list_of_numbers:
        print("*" * 10)
        row = row.replace("\n", "")
        
        print(f"ROW: {row}")
        digit = 0

        while (digit != len(row) - 12):
            thirteen_digit = row[digit:(digit + 13)]
            multi = 1

            print(thirteen_digit)
            
            for number in thirteen_digit:
                multi *= int(number)

            print(f"Multi: {multi}")

            greatest_products.append(multi)
            digit += 1
    
    print(f"Answer: {max(greatest_products)}")

# ANSWER: 23514624000 but I couldn't finddddddd.
# My ANSWER is 5377010688.
