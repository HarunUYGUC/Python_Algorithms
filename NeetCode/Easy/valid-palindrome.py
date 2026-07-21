import string

class Solution:
    def isPalindrome(self, s):
        words = s.split()
        forwardChars = []
        backwardChars = []

        for word in words:
            for char in word:
                # string.punctuation is a string containing all punctuation characters.
                if char not in string.punctuation:
                    forwardChars.append(char.lower())

        backwardChars = forwardChars[::-1]

        if forwardChars == backwardChars:
            return True
        else:
            return False
