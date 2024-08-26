""" https://leetcode.com/problems/rotate-string/ """

class Solution:
    def rotateString(self, s, goal):
        s = list(s)
        goal = list(goal)
        k = 0

        while (k != len(s)):
            temp = s[0]

            for i in range(1, len(s)):
                s[i - 1] = s[i]
                
            s[len(s) - 1] = temp
            k += 1

            if (s == goal):
                return True
        
        return False

print(Solution().rotateString("abcde", "abced"))
