class Solution:
    def findMaxK(self, nums):
        positives = []
        negatives = []

        for num in nums:
            if (num > 0):
                positives.append(num)
            else:
                negatives.append(num)
        
        positives.sort()
        negatives.sort()

        for i in range(len(positives) - 1, -1, -1):
            for j in range(len(negatives)):
                if (positives[i] == -1 * negatives[j]):
                    return positives[i]
        
        return -1

solution = Solution()
print(solution.findMaxK([-25,25,-27,45,31,46,46,21]))
