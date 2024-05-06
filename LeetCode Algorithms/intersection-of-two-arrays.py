""" https://leetcode.com/problems/intersection-of-two-arrays/ """

class Solution:
    def intersection(self, nums1, nums2):
        list = []

        for num in nums1:
            if num in nums2 and num not in list:
                list.append(num)

        return list

print(Solution().intersection([1,2,2,1], [2,2]))
