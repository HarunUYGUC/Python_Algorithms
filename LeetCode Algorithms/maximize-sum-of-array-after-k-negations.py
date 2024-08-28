""" https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/ """

class Solution:
    def largestSumAfterKNegations(self, nums, k):
        minNum = min(nums)
        minNumIndex = nums.index(minNum)
        sum = 0

        if (minNum < 0): # Negatif, Tek veya Çift
            nums[minNumIndex] *= -1
            k -= 1

            while (k > 0) and (minNum < 0): # Negatifler pozitife dönüşene kadar.
                minNum = min(nums)
                minNumIndex = nums.index(minNum)
                nums[minNumIndex] *= -1
                k -= 1
            
            if (k % 2 == 0): # Negatif ve Çift
                pass
            else: # Negatif ve Tek
                nums[minNumIndex] *= -1
        elif (minNum >= 0) and (k % 2 == 0): # Pozitif ve Çift
            pass
        elif (minNum >= 0) and (k % 2 == 1): # Pozitif ve Tek
            nums[minNumIndex] *= -1

        for num in nums:
            sum += num

        return sum

print(Solution().largestSumAfterKNegations([-2,5,0,2,-2], 3))
