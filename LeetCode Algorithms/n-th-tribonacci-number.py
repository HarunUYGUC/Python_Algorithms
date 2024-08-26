""" https://leetcode.com/problems/n-th-tribonacci-number/ """

class Solution:
    def tribonacci(self, n):
        t0, t1, t2 = 0, 1, 1

        if (n == 0):
            return 0
        elif (n == 1) or (n == 2):
            return 1
        else:
            while (n > 2):
                t0, t1, t2 = t1, t2, (t0 + t1 + t2)
                n -= 1
        
            return t2
    
print(Solution().tribonacci(25))
