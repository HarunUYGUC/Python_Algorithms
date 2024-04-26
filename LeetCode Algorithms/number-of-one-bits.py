""" https://leetcode.com/problems/number-of-1-bits/description/ """

class Solution:
    def hammingWeight(self, n):
        binary = "" # Backwards
        count = 0

        while (n > 0):
            binary += str(n % 2)
            n //= 2
        
        for i in binary:
            if (i == "1"):
                count += 1

        return count

solution = Solution()
print(solution.hammingWeight(128))
