""" https://leetcode.com/problems/reverse-words-in-a-string-iii/ """

# Method 1

class Solution:
    def reverseWords(self, s):
        words = s.split()
        reverseWords = ""

        for i in range(len(words)):
            for j in range(len(words[i]) - 1, -1, -1):
                reverseWords += words[i][j]

            # It can also be done this way instead of using rstrip().
            # if (i != len(words) - 1):
            #     reverseWords += " "

            reverseWords += " "

        reverseWords = reverseWords.rstrip()

        return reverseWords

print(Solution().reverseWords("hehe hehe hehe hehe"))


# Method 2

class Solution:
    def reverseWords(self, s):
        words = s.split()
        reverseWords = ""

        for word in words:
            for j in range(len(word) - 1, -1, -1):
                reverseWords += word[j]

            reverseWords += " "

        reverseWords = reverseWords.rstrip()

        return reverseWords

print(Solution().reverseWords("hehe hehe hehe hehe"))
