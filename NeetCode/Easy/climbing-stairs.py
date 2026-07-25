# Dynamic Programming (Top-Down)

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n  # 1. basamak için 1, 2. için ise 2 yol vardır.

        # Her basamağın yol sayısını tutmak için.
        dp = [0] * (n + 1) # dp = [0, 0, 0, 0, 0, 0]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
