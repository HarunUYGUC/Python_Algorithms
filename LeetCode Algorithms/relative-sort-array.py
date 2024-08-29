""" https://leetcode.com/problems/relative-sort-array/ """

class Solution:
    def relativeSortArray(self, arr1, arr2):
        list = []

        for arr in arr2:
            if arr in arr1:
                total = arr1.count(arr)

                while (total != 0):
                    list.append(arr)
                    arr1.remove(arr)
                    total -= 1
            
        arr1.sort()
        list.extend(arr1)
        return list
    
print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
