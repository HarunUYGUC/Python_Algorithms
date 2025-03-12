""" https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/ """

class Solution:
    def maximumCount(self, nums):
        negatives = 0
        positives = 0

        for num in nums:
            if (num < 0):
                negatives += 1
            elif (num > 0):
                positives += 1

        if (negatives > positives):
            return negatives
        else:
            return positives
        
print(Solution().maximumCount([-2,-1,-1,1,2,3]))
