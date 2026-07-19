class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            ext = target - nums[i]

            for j in range(i + 1, len(nums)):
                if (ext == nums[j]):
                    return [i, j]
