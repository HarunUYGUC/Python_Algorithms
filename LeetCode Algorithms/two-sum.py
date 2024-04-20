""" https://leetcode.com/problems/two-sum/ """

class Solution:
    def twoSum(self, nums, target):
        n = 1
        for i in range(len(nums) - 1):
            for j in range(n, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
            n += 1

solution = Solution()
result = solution.twoSum([2,5,5,11], 10)
print(result)
