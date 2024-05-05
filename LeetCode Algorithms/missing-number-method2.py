""" https://leetcode.com/problems/missing-number/ """

# I tried to do it without using "not in".

class Solution:
    def missingNumber(self, nums):
        list = []

        for i in range(len(nums) + 1):
            list.append(i)

        for i in range(len(list)):
            flag = False

            for j in range(len(nums)):
                if (list[i] == nums[j]):
                    nums.pop(j)
                    flag = True
                    break

            if (flag == False):
                return list[i]

solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
