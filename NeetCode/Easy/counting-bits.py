class Solution:
    def countBits(self, n):
        output = []

        for i in range(n + 1):
            output.append(bin(i).count("1"))

        return output
