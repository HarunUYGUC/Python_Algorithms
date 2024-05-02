""" https://leetcode.com/problems/contains-duplicate/ """

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
