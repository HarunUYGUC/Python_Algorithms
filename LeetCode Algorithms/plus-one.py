""" https://leetcode.com/problems/plus-one/description/ """

class Solution:
    def plusOne(self, digits):
        strDigits = ""

        for digit in digits:
            strDigits += str(digit)
        
        intDigits = int(strDigits) + 1
        strDigits = str(intDigits)
        list = []

        for digit in strDigits:
            list.append(int(digit))
        
        return list

solution = Solution()
print(solution.plusOne([4,3,2,1]))
