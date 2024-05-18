""" https://leetcode.com/problems/backspace-string-compare/ """

class Solution:
    def backspaceCompare(self, s, t):
        s = [s[i] for i in range(len(s))]
        t = [t[i] for i in range(len(t))]

        while (s.count("#") != 0):
            index = s.index("#")
            s.pop(index)

            if (index != 0):
                s.pop(index - 1)

        while (t.count("#") != 0):
            index = t.index("#")
            t.pop(index)

            if (index != 0):
                t.pop(index - 1)

        if (len(s) == len(t)):
            for i in range(len(s)):
                if (s[i] != t[i]):
                    return False
            return True
        else:
            return False

print(Solution().backspaceCompare("a#c", "b"))
