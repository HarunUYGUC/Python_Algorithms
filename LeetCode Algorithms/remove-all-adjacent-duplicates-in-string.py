""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/ """

# Output Limit Exceeded
# 45 / 106 testcases passed

class Solution:
    def removeDuplicates(self, s):
        s = list(s)
        length = len(s)
        i = 0

        while (i != length):
            if (i != length - 1) and (s[i] == s[i + 1]):
                s.pop(i)
                s.pop(i)
                length -= 2
                
                if (i != 0):
                    i -= 1
            else:
                i += 1
            
            print("s:", s, "length:", length, "i:", i)

        newS = ""

        for c in s:
            newS += c

        return newS
    
print(Solution().removeDuplicates("aababaab"))
