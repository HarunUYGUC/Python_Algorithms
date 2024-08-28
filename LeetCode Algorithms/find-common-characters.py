""" https://leetcode.com/problems/find-common-characters/ """

class Solution:
    def commonChars(self, words):
        if (len(words) == 1):
            return list(words[0])
        elif (len(words) == 2):
            commons = []

            for i in words[0]:
                if i in words[1]:
                    commons.append(i)
                    words[1] = words[1].replace(i, "_", 1)
            
            return commons
        else:
            firstWord = words[0]
            secondWord = words[1]
            words.pop(0)
            words.pop(0)
            commons = []

            for char in firstWord:
                if char in secondWord:
                    commons.append(char)
                    secondWord = secondWord.replace(char, "_", 1)

            delete = []

            for word in words:
                for common in commons:
                    if common in word:
                        word = word.replace(common, "*", 1)
                    else:
                        delete.append(common)

                if (len(delete) != 0):
                    for delet in delete:
                        commons.remove(delet)

                delete.clear()

            return commons
    
print(Solution().commonChars(["daaccccd","adacbdda","abddbaba","bacbcbcb","bdaaaddc","cdadacba","bacbdcda","bacdaacd"]))
