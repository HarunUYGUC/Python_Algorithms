""" https://leetcode.com/problems/last-stone-weight/ """

class Solution:
    def lastStoneWeight(self, stones):
        while (len(stones) > 1):
            firstMaxStone = max(stones)
            stones.remove(firstMaxStone)

            secondMaxStone = max(stones)
            stones.remove(secondMaxStone)

            if (firstMaxStone > secondMaxStone):
                stones.append(firstMaxStone - secondMaxStone)

            print(stones)

        if (len(stones) == 0):
            return 0
        else:
            return stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8,1]))
