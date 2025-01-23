""" https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ """

# Time Limit Exceeded
# 42 / 90 testcases passed

class Solution:
    def replaceElements(self, arr):
        newArr = []

        for i in range(len(arr) - 1):
            max = arr[i + 1]

            for j in range(i + 1, len(arr) - 1):
                if (arr[j + 1] > max):
                    max = arr[j + 1]
                
            newArr.append(max)

        newArr.append(-1)
        return newArr
    
print(Solution().replaceElements([17,18,5,4,6,1]))
