""" https://leetcode.com/problems/find-numbers-with-even-number-of-digits/ """

class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if (len(str(num)) % 2 == 0):
                count += 1

        return count
    
print(Solution().findNumbers([555,901,482,1771]))
