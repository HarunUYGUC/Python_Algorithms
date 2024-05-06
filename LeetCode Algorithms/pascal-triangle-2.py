""" https://leetcode.com/problems/pascals-triangle-ii/ """

class Solution:
    def getRow(self, rowIndex):
        newList = []

        if (rowIndex == 0):
            return [1]
        elif (rowIndex == 1):
            return [1,1]
        else:
            list = [[1,1]]

            while (rowIndex > 1):
                newList = []

                for i in range(len(list[0])):
                    if (i == 0):
                        newList.append(1)
                    else:
                        newList.append(list[0][i] + list[0][i - 1])

                newList.append(1)
                list = []
                list.append(newList)
                rowIndex -= 1

        return newList

print(Solution().getRow(3))
