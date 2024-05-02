""" https://leetcode.com/problems/power-of-two/ """

class Solution:
    def isPowerOfTwo(self, n):
        product = 1

        while (product <= n):
            if (product == n):
                return True
            else:
                product *= 2
        
        return False

solution = Solution()
print(solution.isPowerOfTwo(9))
