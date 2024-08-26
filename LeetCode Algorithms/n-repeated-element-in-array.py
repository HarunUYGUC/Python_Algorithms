""" https://leetcode.com/problems/n-repeated-element-in-size-2n-array/ """

class Solution:
    def repeatedNTimes(self, nums):
        for num in nums:
            x = nums.count(num)

            if (x > 1):
                return num
            
print(Solution().repeatedNTimes([1,2,3,3]))
