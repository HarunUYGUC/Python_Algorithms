""" https://leetcode.com/problems/add-digits/ """

class Solution:
    def addDigits(self, num):
        if (num // 10 == 0):
            return num
        
        while (len(str(num)) != 1):
            sum = 0
            
            while (num > 0):
                digit = num % 10
                num //= 10
                sum += digit
            
            num = sum
                    
        return num

solution = Solution()
print(solution.addDigits(38))
