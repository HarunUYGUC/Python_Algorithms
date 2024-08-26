""" https://leetcode.com/problems/toeplitz-matrix/ """

# 364 / 483 testcases passed

class Solution:
    def isToeplitzMatrix(self, matrix):
        if (len(matrix) > len(matrix[0])):
            length = len(matrix[0])
        elif (len(matrix) < len(matrix[0])):
            length = len(matrix)
        else:
            length = len(matrix)

        numbers = []

        for i in range(length):
            numbers.append(matrix[i][i])
        
        piece = numbers.count(numbers[0])

        if (piece == length):
            return True
        else:
            return False
        
print(Solution().isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))
