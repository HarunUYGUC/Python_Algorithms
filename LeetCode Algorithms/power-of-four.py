""" https://leetcode.com/problems/power-of-four/ """

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        product = 1

        while (product <= n):
            if (product == n):
                return True
            else:
                product *= 4
        
        return False

solution = Solution()
print(solution.isPowerOfFour(16))
