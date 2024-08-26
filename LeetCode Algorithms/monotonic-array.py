""" https://leetcode.com/problems/monotonic-array/ """

class Solution:
    def isMonotonic(self, nums):
        
        # Decreasing
        decreasing = True

        for i in range(len(nums) - 1):
            if (nums[i] < nums[i + 1]):
                decreasing = False
                break

        # Increasing
        increasing = True

        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                increasing = False
                break

        if (decreasing == False) and (increasing == False):
            return False
        else:
            return True
        
print(Solution().isMonotonic([6,5,4,4]))
