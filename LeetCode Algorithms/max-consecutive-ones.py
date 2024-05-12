""" https://leetcode.com/problems/max-consecutive-ones/ """

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        temp = 0

        for num in nums:
            if (num == 1):
                count += 1
            else:
                if (count > temp):
                    temp = count
                
                count = 0

        if (count > temp):
            temp = count

        return temp
    
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
