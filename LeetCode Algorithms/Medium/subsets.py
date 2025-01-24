""" https://leetcode.com/problems/subsets/ """

class Solution:
    def subsets(self, nums):
        nums = sorted(nums)

        if (len(nums) == 1):
            return [[], nums]
        elif (len(nums) == 2):
            return [[], [nums[0]], [nums[1]], nums]
        else:
            subsets = []
            subsets.append([])

            for i in range(len(nums) - 1):
                subsets.append([nums[i]])

                for j in range(i + 1, len(nums)):
                    subsets.append([nums[i], nums[j]])

            subsets.append([nums[len(nums) - 1]])
            subsets.append(nums)
            return subsets

print(Solution().subsets([1,2,3]))
