""" https://leetcode.com/problems/find-pivot-index/ """

class Solution:
    def pivotIndex(self, nums):
        sumAll = 0

        for num in nums:
            sumAll += num

        for i in range(len(nums)):            
            if (i > 0) and (i < len(nums) - 1):
                rightSum -= nums[i]
                leftSum += nums[i - 1]
            elif (i == 0):
                leftSum = 0
                rightSum = sumAll - nums[i]
            elif (i == len(nums) - 1):
                leftSum = sumAll - nums[i]
                rightSum = 0

            if (leftSum == rightSum):
                return i
                
        return -1
    
print(Solution().pivotIndex([1,7,3,6,5,6]))
