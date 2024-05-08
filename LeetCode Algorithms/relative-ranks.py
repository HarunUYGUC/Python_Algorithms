""" https://leetcode.com/problems/relative-ranks/ """

class Solution:
    def findRelativeRanks(self, score):
        firstThreeRanks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = 0
        ranks = []
        i = 0
        
        while (i < len(score)):
            ranks.append(0)
            i += 1

        while (n < len(score)):
            personScore = max(score)
            personIndex = score.index(personScore)

            if (n < 3):
                ranks[personIndex] = firstThreeRanks[n]
            else:
                ranks[personIndex] = str(n + 1)
            
            score[personIndex] = -1
            n += 1

        return ranks

print(Solution().findRelativeRanks([5,4,3,2,1]))
