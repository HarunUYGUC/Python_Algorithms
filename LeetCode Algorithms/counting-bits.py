""" https://leetcode.com/problems/counting-bits/ """

class Solution:
    def countBits(self, n):
        list = []

        for i in range(n + 1):
            binary = "" # Backwards
            count = 0

            while (i > 0):
                binary += str(i % 2)
                i //= 2

            for i in binary:
                if (i == "1"):
                    count += 1

            list.append(count)

        return list
    
solution = Solution()
print(solution.countBits(5))
