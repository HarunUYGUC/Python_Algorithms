""" For the example from Project Euler, see the other example below, not this one! """

# In this example, I selected the largest numbers in the rows, added them with the largest numbers in the other rows, and printed the result.
"""
   3       # 3
  7 4      # 7
 2 4 6     # 6
8 5 9 3    # 9
"""

rows = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
sum = 0

for row in rows:
    biggest = 0
    
    for i in range(len(row)):
        if (row[i] > biggest):
            biggest = row[i]
    
    print(biggest)
    sum += biggest

print(sum)



""" https://projecteuler.net/problem=18 """

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
"""
   3       # 3
  7 4      # 7
 2 4 6     # 4
8 5 9 3    # 9
"""
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:

# Method 1

rows = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34,], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], 
        [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,], 
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
sum = 0

for row in rows:
    if (len(row) > 1):
        biggest = row[index_of_biggest]
        index_of_biggest = index_of_biggest

        if (row[index_of_biggest + 1] > biggest):
            biggest = row[index_of_biggest + 1]
            index_of_biggest = index_of_biggest + 1
    else:
        biggest = row[0]
        index_of_biggest = 0
        
    print(f"Biggest Index: {index_of_biggest}")
    print(f"Biggest Number: {biggest}")
    sum += biggest

print(f"Sum: {sum}")

# I find 1064 but the answer is 1074. I still don't understand how it happens because I checked it one by one and it should be 1064.


# Method 2

# I find 1064 but the answer is 1074. I still don't understand how it happens because I checked it one by one and it should be 1064.

rows = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34,], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], 
        [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,], 
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

sum = rows[0][0]
idOfLargest = 0
 
for i in range(1, len(rows)):

    if (idOfLargest == len(rows[i]) - 1):
        bigger = idOfLargest
        smaller = bigger - 1
    else:
        smaller = idOfLargest
        bigger = idOfLargest + 1
        
    if (rows[i][smaller] > rows[i][bigger]):
        idOfLargest = smaller
        sum += rows[i][smaller]
    else:
        idOfLargest = bigger
        sum += rows[i][bigger]

print(sum)
