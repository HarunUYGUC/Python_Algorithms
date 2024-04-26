""" https://leetcode.com/problems/valid-anagram/ """

# Method 1

class Solution:
    def isAnagram(self, s, t):
        if (len(s) < len(t)):
            return False
        
        s = list(s)
        t = list(t)

        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
            
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))


# Method 2

class Solution:
    def isAnagram(self, s, t):
        if (len(s) < len(t)):
            return False

        for i in s:
            x = s.count(i)
            y = t.count(i)

            if (x != y):
                return False
            
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
