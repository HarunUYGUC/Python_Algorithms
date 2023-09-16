"""
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromic_numbers = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        multiplication = str(i * j)

        if (len(multiplication) == 6):
            if (multiplication == multiplication[::-1]):
                palindromic_numbers.append(multiplication)
        
biggest_pal_num = palindromic_numbers[0]

for pal_num in palindromic_numbers:
    if (biggest_pal_num < pal_num):
        biggest_pal_num = pal_num

print(biggest_pal_num)

""" Instead of doing it as above, we can do it faster with the max() list method.
But dealing with it as above shows that you know this subject better. """
# print(max(palindromic_numbers))
