""" https://leetcode.com/problems/find-pivot-index/ """

# 739 / 746 testcases passed

class Solution:
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if (i == 0):
                leftSum = 0
                rightSum = 0

                for j in range(1, len(nums)):
                    rightSum += nums[j]
                
                if (leftSum == rightSum):
                    return i
            elif (i == len(nums) - 1):
                leftSum = 0
                rightSum = 0

                for j in range(len(nums) - 2, -1, -1):
                    leftSum += nums[j]

                if (leftSum == rightSum):
                    return i
            else:
                leftSum = 0
                rightSum = 0

                for j in range(i + 1, len(nums)):
                    rightSum += nums[j]
                
                for j in range(i - 1, -1, -1):
                    leftSum += nums[j]

                if (leftSum == rightSum):
                    return i

        return -1
    
print(Solution().pivotIndex([2,1,-1]))
