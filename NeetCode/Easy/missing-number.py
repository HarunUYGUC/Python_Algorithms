class Solution:
    def missingNumber(self, nums):
        for num in range(len(nums) + 1):
            if num not in nums:
                return num
