""" https://leetcode.com/problems/longest-common-prefix/ """

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        first = strs[0]
        strs.pop(0)
        firstLen = len(first)

        for str in strs:
            othersLen = len(str)

            if (firstLen > othersLen):
                size = othersLen
            else:
                size = firstLen

            for i in range(size - 1):
                if (str[i] == first[i]):
                    prefix += str[i]
                else:
                    break
            
        if (prefix == 0):
            print("")
        else:
            print(prefix)

solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)
