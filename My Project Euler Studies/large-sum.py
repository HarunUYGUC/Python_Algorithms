# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. In the large-sum.txt file.

sum = 0

with open(r"C:\Users\Harun\Desktop\Python-Algoritmalarim\My Project Euler Studies\large-sum.txt") as file:
    list_of_numbers = file.readlines()

    for row in list_of_numbers:
        sum += int(row)

    first_ten_digits = str(sum)[0:10]

    print(f"First Ten Digits of the Sum: {first_ten_digits}")
