""" https://leetcode.com/problems/maximum-product-of-three-numbers/ """

class Solution:
    def maximumProduct(self, nums):
        numsCopy = nums.copy()
        n = 0
        threePozitiveProduct = 1
        
        while (n < 3):
            maxNum = max(numsCopy)
            threePozitiveProduct *= maxNum
            numsCopy.remove(maxNum)
            n += 1
        
        twoNegativeOnePozitiveProduct = 1
        n = 0

        while (n < 2):
            minNum = min(nums)
            twoNegativeOnePozitiveProduct *= minNum
            nums.remove(minNum)
            n += 1
        
        maxNum = max(nums)
        twoNegativeOnePozitiveProduct *= maxNum

        if (threePozitiveProduct > twoNegativeOnePozitiveProduct):
            return threePozitiveProduct
        else:
            return twoNegativeOnePozitiveProduct
            
print(Solution().maximumProduct([-100,-98,-1,2,3,4]))
