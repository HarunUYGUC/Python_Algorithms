with open(r"C:\Users\Harun\Desktop\Python_Algorithms\My Project Euler Studies\largest-product-in-a-series.txt") as file:
    list_of_numbers = file.readlines()
    greatest_products = []

    for row in list_of_numbers:
        print("*" * 10)

        # new_row = []

        # for number in row:
        #     if (number != '\n'):
        #         row.append(number)
        
        row = row.replace("\n", "") # Instead of doing it like in the comment line, we can do it this way.

        print(f"ROW: {row}")
        digit = 0

        while (digit != len(row) - 3):
            thirteen_digit = row[digit:(digit + 4)]
            multi = 1

            print(thirteen_digit)
            
            for number in thirteen_digit:
                multi *= int(number)

            print(f"Multi: {multi}")

            greatest_products.append(multi)
            digit += 1
    
    print(f"Answer: {max(greatest_products)}")




# str = "73167176531330624919225119674426574742355349194934\
#     96983520312774506326239578318016984801869478851843\
#     85861560789112949495459501737958331952853208805511\
#     12540698747158523863050715693290963295227443043557\
#     66896648950445244523161731856403098711121722383113"

# \ => Çok satırlı stringlerde yeni satır. Bu kaçış karakteri 4 karakterlik yer kaplıyor.

# str = "Harun\
#     Uyguç\
#     20\
#     PC Müh"

# print(str)
# print(len(str))
# print(str[7])

# str = "Harun\
#     Uyguç\
#     "

# print(str)
# print(len(str))
# print(str[7])

# str = "Harun\
#     Uyguç"

# print(str)
# print(len(str))
# print(str[7])

# str = "Harun Uyguç 20 PC Müh"

# print(str)
# print(len(str))
# print(str[7])

# str = "HarunUyguç20PCMüh"

# print(str)
# print(len(str))
# print(str[7])
