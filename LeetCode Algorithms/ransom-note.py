""" https://leetcode.com/problems/ransom-note/ """

# Method 1 (Not Bad)

class Solution:
    def canConstruct(self, ransomNote, magazine):
        if (len(magazine) < len(ransomNote)):
            return False

        for c in ransomNote:
            count1 = ransomNote.count(c)
            count2 = magazine.count(c)

            if (count1 <= count2):
                pass
            else:
                return False
            
        return True

print(Solution().canConstruct("aa", "aab"))


# Method 2 (Good)

class Solution:
    def canConstruct(self, ransomNote, magazine):
        if (len(magazine) < len(ransomNote)):
            return False
        
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        for c in ransomNote:
            if c in magazine:
                magazine.remove(c)
            else:
                return False
        
        return True

print(Solution().canConstruct("aa", "aab"))
