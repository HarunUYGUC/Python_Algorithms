""" https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/ """
# My code passed about 30 of 34 tests.

class Solution:
    def findDisappearedNumbers(self, nums):
        list = []

        for i in range(1, len(nums) + 1):
            if i not in nums:
                list.append(i)
 
        return list

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
