""" https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/ """

class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if (needle[0] == haystack[i]):
                if (needle == haystack[i: i + len(needle)]):
                    return i        
        return -1
            
solution = Solution()
print(solution.strStr("abc", "c"))
