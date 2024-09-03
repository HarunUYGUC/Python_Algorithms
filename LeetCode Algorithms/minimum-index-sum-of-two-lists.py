""" https://leetcode.com/problems/minimum-index-sum-of-two-lists/ """

class Solution:
    def findRestaurant(self, list1, list2):
        commons = []
        list1Indexes = []
        list2Indexes = []

        for str in list1:
            if str in list2:
                commons.append(str)
                list1Indexes.append(list1.index(str))
                list2Indexes.append(list2.index(str))

        if (len(commons) <= 1):
            return commons
        else:
            leastCommons = []
            least = list1Indexes[0] + list2Indexes[0]
            leastCommons.append(commons[0])

            for i in range(1, len(commons)):
                sum = list1Indexes[i] + list2Indexes[i]

                if (sum < least):
                    least = sum
                    leastCommons.clear()
                    leastCommons.append(commons[i])
                elif (sum == least):
                    least = sum
                    leastCommons.append(commons[i])

            return leastCommons
            
print(Solution().findRestaurant(["happy","sad","good"], ["sad","happy","good"]))
