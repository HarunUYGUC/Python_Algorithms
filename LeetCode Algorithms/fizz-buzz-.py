""" https://leetcode.com/problems/fizz-buzz/ """

class Solution:
    def fizzBuzz(self, n):
        list = []
        i = 1

        while (i <= n):
            if (i % 3 == 0) and (i % 5 == 0):
                list.append("FizzBuzz")
            elif (i % 5 == 0):
                list.append("Buzz")
            elif (i % 3 == 0):
                list.append("Fizz")
            else:
                list.append(f"{i}")

            i += 1
        
        return list

print(Solution().fizzBuzz(15))
