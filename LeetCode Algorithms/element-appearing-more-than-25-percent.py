""" https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/ """

class Solution:
    def findSpecialInteger(self, arr):
        nums = []
        freqs = []

        for num in arr:
            if num not in nums:
                nums.append(num)
                freqs.append(1)
            else:
                freqs[nums.index(num)] += 1

        totalFreqs = sum(freqs)

        for freq in freqs:
            if (freq / totalFreqs > 0.25):
                return nums[freqs.index(freq)]
            
print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))
