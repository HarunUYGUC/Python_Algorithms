""" https://leetcode.com/problems/reverse-string/ """

class Solution:
    def reverseString(self, s):
        repetition = len(s) // 2
        start = 0
        end = len(s) - 1

        while (repetition > 0):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            repetition -= 1
        
        return s

solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))
