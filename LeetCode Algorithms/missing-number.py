""" https://leetcode.com/problems/missing-number/ """

class Solution:
    def missingNumber(self, nums):
        list = []

        for i in range(len(nums) + 1):
            list.append(i)
        
        for j in list:
            if j not in nums:
                return j

solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
