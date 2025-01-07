""" https://leetcode.com/problems/unique-number-of-occurrences/ """

class Solution:
    def uniqueOccurrences(self, arr):
        newArr = []
        freqs = []

        for num in arr:
            if num not in newArr:
                newArr.append(num)

        for num in newArr:
            freqs.append(arr.count(num))

        for freq in freqs:
            if (freqs.count(freq) > 1):
                return False

        return True
            
print(Solution().uniqueOccurrences([-5,-6,2,6,-5,-7,5]))
