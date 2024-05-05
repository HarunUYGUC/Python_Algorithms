""" https://leetcode.com/problems/power-of-three/ """

class Solution:
    def isPowerOfThree(self, n):
        product = 1

        while (product <= n):
            if (product == n):
                return True
            else:
                product *= 3
        
        return False

solution = Solution()
print(solution.isPowerOfThree(27))
