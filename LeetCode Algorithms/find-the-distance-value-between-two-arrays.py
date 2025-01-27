""" https://leetcode.com/problems/find-the-distance-value-between-two-arrays/ """

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        willRemove = []

        for i in arr1:
            for j in arr2:
                if (abs(i - j) <= d):
                    willRemove.append(i)
                    break

        for i in willRemove:
            arr1.remove(i)

        return len(arr1)
    
print(Solution().findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))
