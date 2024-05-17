""" https://leetcode.com/problems/jewels-and-stones/ """

class Solution:
    def numJewelsInStones(self, jewels, stones):
        sum = 0

        for jewel in jewels:
            if jewel in stones:
                sum += stones.count(jewel)
        
        return sum

print(Solution().numJewelsInStones("aA", "aAAbbbb"))
