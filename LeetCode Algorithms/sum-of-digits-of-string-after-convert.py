""" https://leetcode.com/problems/sum-of-digits-of-string-after-convert/ """

class Solution:
    def getLucky(self, s, k):
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        newS = ""

        for c in s:
            newS += str(alphabet.index(c) + 1)

        while (k != 0):
            sum = 0

            for i in newS:
                sum += int(i)

            newS = str(sum)
            k -= 1
        
        return int(newS)

print(Solution().getLucky("zbax", 2))
