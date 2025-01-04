""" https://leetcode.com/problems/height-checker/ """

class Solution:
    def heightChecker(self, heights):
        count = 0
        expectedHeights = sorted(heights)

        for i in range(len(heights)):
            if (heights[i] != expectedHeights[i]):
                count += 1
            
        return count

print(Solution().heightChecker([1,1,4,2,1,3]))
