""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """
# My code passed about 200 of 212 tests.

class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(len(prices) - 1):
            buy = prices[0]
            prices.pop(0)
            
            dif = max(prices) - buy
                
            if (dif > profit):
                profit = dif

        return profit
    
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
