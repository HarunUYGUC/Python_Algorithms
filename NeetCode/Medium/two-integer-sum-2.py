class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        total = numbers[left] + numbers[right]

        while (total != target):
            if (total > target):
                right -= 1
            elif (total < target):
                left += 1
            
            total = numbers[left] + numbers[right]
            
        return [left + 1, right + 1]
