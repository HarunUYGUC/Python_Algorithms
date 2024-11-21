""" https://leetcode.com/problems/uncommon-words-from-two-sentences/ """

class Solution:
    def uncommonFromSentences(self, s1, s2):
        uncommonWords = []
        s1 = s1.split()
        s2 = s2.split()

        if (len(s1) >= len(s2)):
            string = s2
        else:
            string = s1

        for word in string:
            pieceS1 = s1.count(word)

            print("başta", word)

            if (pieceS1 > 1):
                continue
            else:
                pieceS2 = s2.count(word)

                if (pieceS2 > 0):
                    continue
                else:
                    uncommonWords.append(word)
            
            print("sonda", word)



        return uncommonWords
    
print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))
