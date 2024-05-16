""" https://leetcode.com/problems/reshape-the-matrix/ """

import numpy as np

class Solution:
    def matrixReshape(self, mat, r, c):
        if (len(mat) * len(mat[0]) == r * c):
            oneDimenMat = []

            for row in mat:
                for num in row:
                    oneDimenMat.append(num)

            newMatrix = np.arange(r * c).reshape(r, c)
            n = 0

            for i in range(len(newMatrix)):
                for j in range(len(newMatrix[0])):
                    newMatrix[i][j] = oneDimenMat[n]
                    n += 1

            return newMatrix
        else:
            return mat

print(Solution().matrixReshape([[1,2],[3,4]], 1, 4))
