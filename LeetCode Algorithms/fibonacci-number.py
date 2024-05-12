""" https://leetcode.com/problems/fibonacci-number/ """

class Solution:
    def fib(self, n):
        if (n == 0):
            return 0
        elif (n == 1) or (n == 2):
            return 1
        else:
            a, b = 1, 1
            i = 3

            while (i <= n):
                a, b = b, a + b
                i += 1
            
            return b

print(Solution().fib(3))
