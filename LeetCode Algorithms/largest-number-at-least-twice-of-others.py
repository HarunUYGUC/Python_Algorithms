""" https://leetcode.com/problems/largest-number-at-least-twice-of-others/ """

class Solution:
    def dominantIndex(self, nums):
        maxNum = max(nums)
        indexOfMaxNum = nums.index(maxNum)
        nums.remove(maxNum)

        for num in nums:
            if (2*num > maxNum):
                return -1
            
        return indexOfMaxNum

print(Solution().dominantIndex([3,6,1,0]))
