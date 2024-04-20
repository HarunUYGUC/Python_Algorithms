""" https://leetcode.com/problems/search-insert-position/ """

class Solution:
    def searchInsert(self, nums, target):
        index = 0
        for num in nums:
            if (num == target):
                return index
            if (num > target):
                return index
            index += 1

        return index

solution = Solution()
print(solution.searchInsert([1,3,5,6], 7))
