""" https://leetcode.com/problems/valid-parentheses/ """
# My code passed about 71 of 98 tests.

class Solution:
    def isValid(self, s):
        flag = True

        for i in range(0, len(s) - 1, 2):
            if (s[i] == "(") and (s[i + 1] == ")"):
                pass
            elif (s[i] == "[") and (s[i + 1] == "]"):
                pass
            elif (s[i] == "{") and (s[i + 1] == "}"):
                pass
            else:
                return False
        
        if (flag == True):
            return True

solution = Solution()
print(solution.isValid("()[]{}"))
