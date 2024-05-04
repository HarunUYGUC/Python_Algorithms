""" https://leetcode.com/problems/move-zeroes/ """

class Solution:
    def moveZeroes(self, nums):
        i = 0
        countZeros = 0
        start = 0

        while (i < len(nums) - 1):
            for j in range(start, len(nums) - 1 - countZeros):
                if (nums[j] == 0):
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                else:
                    start += 1
            
            countZeros += 1
            i += 1

        return nums

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
