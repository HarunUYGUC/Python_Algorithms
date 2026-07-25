class Solution:
    def singleNumber(self, nums):
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for key, value in dic.items():
            if (value == 1):
                return key
