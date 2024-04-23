""" https://leetcode.com/problems/longest-common-prefix/description/ """

class Solution:
    def longestCommonPrefix(self, strs):
        first = strs[0]
        strs.pop(0)
        prefix = ""
        n = -1

        for c in first: 
            count = 0
            n += 1

            for str in strs:
                if (n <= len(str) - 1):
                    if (c == str[n]):
                        count += 1
                else:
                    break
            
            if (count == len(strs)):
                prefix += c
            else:
                break
                
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
