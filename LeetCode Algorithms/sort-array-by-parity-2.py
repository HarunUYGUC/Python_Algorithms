""" https://leetcode.com/problems/sort-array-by-parity-ii/ """

class Solution:
    def sortArrayByParityII(self, nums):
        evenNumbers = []
        oddNumbers = []
        newNums = []

        for num in nums:
            if (num % 2 == 0):
                evenNumbers.append(num)
            else:
                oddNumbers.append(num)
        
        for i in range(len(evenNumbers)):
            newNums.append(evenNumbers[i])
            newNums.append(oddNumbers[i])

        return newNums
    
print(Solution().sortArrayByParityII([4,2,5,7]))
