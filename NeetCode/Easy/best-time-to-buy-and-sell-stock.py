class Solution:
    def maxProfit(self, prices):
        minPrice = float("inf") # Sonsuz
        maxProfit = 0

        for price in prices:
            if (price < minPrice):
                minPrice = price
            elif (price - minPrice > maxProfit):
                maxProfit = price - minPrice
        
        return maxProfit
