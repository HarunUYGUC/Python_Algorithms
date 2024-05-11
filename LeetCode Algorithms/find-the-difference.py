""" https://leetcode.com/problems/find-the-difference/ """

class Solution:
    def findTheDifference(self, s, t):
        for c in t:
            if c not in s:
                return c
            else:
                s = s.replace(c, ",", 1)
            
print(Solution().findTheDifference("a", "aa"))
