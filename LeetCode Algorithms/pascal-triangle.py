""" https://leetcode.com/problems/pascals-triangle/ """

class Solution:
    def generate(self, numRows):
        if (numRows == 1):
            list = [[1]]
        elif (numRows == 2):
            list = [[1],[1,1]]
        else:
            list = [[1],[1,1]]
            count = 1 # To move in inner arrays.

            while (numRows > 2):
                newList = []

                for i in range(len(list)):
                    if (i == 0):
                        newList.append(1)
                    else:
                        newList.append(list[count][i] + list[count][i - 1])

                newList.append(1)
                list.append(newList)
                count += 1   
                numRows -= 1

        return list
    
print(Solution().generate(5))
