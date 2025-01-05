""" https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/ """

class Solution:
    def countCharacters(self, words, chars):
        count = 0

        for word in words:
            flag = True

            for char in word:
                numberOfCharInChars = chars.count(char)
                numberOfCharInWord = word.count(char)

                if (numberOfCharInWord > numberOfCharInChars):
                    flag = False
                    break
                else:
                    index = chars.find(char)

                    if (index == -1):
                        flag = False
                        break

            if (flag == True):
                count += len(word)

        return count
    
print(Solution().countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
