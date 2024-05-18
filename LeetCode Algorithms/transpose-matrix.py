""" https://leetcode.com/problems/transpose-matrix/ """

# Both methods are very close to each other in terms of speed and memory usage, 
# but the first method is slightly better.

# Method 1

import numpy as np

class Solution:
    def transpose(self, matrix):
        transposeMatrix = np.arange(len(matrix) * len(matrix[0])).reshape(len(matrix[0]), len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposeMatrix[j][i] = matrix[i][j]
        
        return transposeMatrix
    
print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))


# Method 2

class Solution:
    def transpose(self, matrix):
        transposeMatrix = []

        # I created an empty list compatible with the transpose of the given matrix.
        for i in range(len(matrix[0])):
            transposeMatrix.append([])

            for j in range(len(matrix)):
                transposeMatrix[i].append(0)
        
        # I filled the empty list with the transpose of the matrix.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposeMatrix[j][i] = matrix[i][j]
        
        return transposeMatrix
    
print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
