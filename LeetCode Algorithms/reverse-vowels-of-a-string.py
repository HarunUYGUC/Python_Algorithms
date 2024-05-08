""" https://leetcode.com/problems/reverse-vowels-of-a-string/ """

class Solution:
    def reverseVowels(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        list = []
        newS = ""

        for c in s:
            if c in vowels:
                list.append(c)
        
        list.reverse()
        length = 0

        for i in range(len(s)):
            if s[i] in vowels:
                newS += list[length]
                length += 1
            else:
                newS += s[i]
        
        return newS

print(Solution().reverseVowels("hello"))
