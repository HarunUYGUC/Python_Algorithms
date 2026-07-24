class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()
        longest = 1
        currentStreak = 1

        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                continue
            
            if (nums[i] + 1 == nums[i + 1]):
                currentStreak += 1
            else:
                longest = max(longest, currentStreak)
                currentStreak = 1

        return max(longest, currentStreak)

solution = Solution()
nums = [2, 20, 4, 10, 3, 4, 5]
print(solution.longestConsecutive(nums))
