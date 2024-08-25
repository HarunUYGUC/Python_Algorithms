""" https://leetcode.com/problems/find-smallest-letter-greater-than-target/ """

class Solution:
    def nextGreatestLetter(self, letters, target):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        targetIndex = alphabet.index(target)

        for letter in letters:
            letterIndex = alphabet.index(letter)

            if (letterIndex > targetIndex):
                return letter
        
        return letters[0]
    
print(Solution().nextGreatestLetter(["x","x","y","y"], "z"))
