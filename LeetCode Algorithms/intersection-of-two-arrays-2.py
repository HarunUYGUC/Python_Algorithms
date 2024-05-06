""" https://leetcode.com/problems/intersection-of-two-arrays-ii/ """

class Solution:
    def intersect(self, nums1, nums2):
        list = []

        for num in nums1:
            if num in nums2:
                list.append(num)
                nums2.remove(num)

        return list

print(Solution().intersect([1,2,2,1], [2]))
