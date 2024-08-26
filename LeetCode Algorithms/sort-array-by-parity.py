""" https://leetcode.com/problems/sort-array-by-parity/ """

class Solution:
    def sortArrayByParity(self, nums):
        evenNumbers = []
        oddNumbers = []

        for num in nums:
            if (num % 2 == 0):
                evenNumbers.append(num)
            else:
                oddNumbers.append(num)
        
        evenNumbers.extend(oddNumbers)
        return evenNumbers
    
print(Solution().sortArrayByParity([3,1,2,4]))
