""" https://leetcode.com/problems/valid-palindrome/ """

class Solution:
    def isPalindrome(self, s):
        newS = ""
        reverseS = ""

        for i in s:        
            if (i.isalnum() == True):
                newS += i.lower()

        for i in range(len(newS) - 1, -1, -1):
            reverseS += newS[i]
        
        if (newS == reverseS):
            return True
        else:
            return False

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
