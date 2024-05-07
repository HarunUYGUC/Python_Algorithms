""" https://leetcode.com/problems/sqrtx/ """

class Solution:
    def mySqrt(self, x):
        product = 1

        while (product*product <= x):
                product += 1
        
        return product - 1
        
print(Solution().mySqrt(27))
