""" https://leetcode.com/problems/single-number/ """

class Solution:
    def singleNumber(self, nums):
        while (len(nums) > 1):
            for num in nums:
                nums.remove(num)

                if num in nums:
                    nums.remove(num)
                else:
                    return num
        
        return nums[0]

print(Solution().singleNumber([2,2,1]))
