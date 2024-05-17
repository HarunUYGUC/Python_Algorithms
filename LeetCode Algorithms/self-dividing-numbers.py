""" https://leetcode.com/problems/self-dividing-numbers/ """

class Solution:
    def selfDividingNumbers(self, left, right):
        list = []

        for num in range(left, right + 1):
            flag = True
            numCopy = num

            while (numCopy > 0):
                digit = numCopy % 10

                if (digit == 0):
                    flag = False
                    break

                numCopy //= 10

                if (num % digit != 0):
                    flag = False
                    break
            
            if (flag == True):
                list.append(num)
        
        return list
    
print(Solution().selfDividingNumbers(1, 22))
