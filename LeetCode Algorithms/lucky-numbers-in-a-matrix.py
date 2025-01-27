""" https://leetcode.com/problems/lucky-numbers-in-a-matrix/ """

class Solution:
    def luckyNumbers(self, matrix):
        mins = []

        for array in matrix:
            minArray = min(array)
            minIndex = array.index(minArray)
            mins.append([minIndex, minArray])

        maxs = []

        for i in range(len(matrix[0])):
            max = 0

            for j in range(len(matrix)):
                if (matrix[j][i] > max):
                    max = matrix[j][i]
                    maxIndex = i

            maxs.append([maxIndex, max])

        for minArr in mins:
            if minArr in maxs:
                return [minArr[1]]

        return []

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
