""" https://leetcode.com/problems/palindrome-number/description/ """

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        newX = ""
        
        for i in range(len(x) - 1, -1, -1):
            newX += x[i]
        
        if (x == newX):
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(121))
