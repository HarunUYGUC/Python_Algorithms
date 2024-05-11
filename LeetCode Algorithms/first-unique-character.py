""" https://leetcode.com/problems/first-unique-character-in-a-string/ """

# Method 1 (Not Bad)

class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            char = s[i]
            s = s.replace(char, ",", 1)

            if char not in s:
                return i

            s = s.replace(",", char)
        
        return -1
            
print(Solution().firstUniqChar("leetcode"))


# Method 2 (Good)

class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s[i] not in s[i + 1::] and s[i] not in s[:i:]:
                return i
            
        return -1
            
print(Solution().firstUniqChar("loveleetcode"))
