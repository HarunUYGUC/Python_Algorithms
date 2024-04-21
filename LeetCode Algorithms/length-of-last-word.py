""" https://leetcode.com/problems/length-of-last-word/ """

class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        words = s.split(" ")
        last = len(words[len(words) - 1])
        return last

solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
