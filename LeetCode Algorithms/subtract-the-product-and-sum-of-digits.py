""" https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/ """

class Solution:
    def subtractProductAndSum(self, n):
        strN = str(n)
        product = 1
        sum = 0

        for c in strN:
            product *= int(c)
            sum += int(c)

        return product - sum
    
print(Solution().subtractProductAndSum(234))
