""" https://leetcode.com/problems/add-to-array-form-of-integer/ """

import sys

sys.set_int_max_str_digits(11000)

class Solution:
    def addToArrayForm(self, num, k):
        strNum = ""

        for c in num:
            strNum += str(c)

        intNum = int(strNum)
        newStrNum = str(intNum + k)
        newNum = []

        for num in newStrNum:
            newNum.append(int(num))
        
        return newNum

print(Solution().addToArrayForm([2,1,5], 806))
