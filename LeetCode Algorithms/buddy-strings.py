""" https://leetcode.com/problems/buddy-strings/ """

# 34 / 39 testcases passed

class Solution:
    def buddyStrings(self, s, goal):
        newS = ""

        if (len(s) != len(goal)):
            return False
        elif (len(s) == 2):
            newS += s[1]
            newS += s[0]

            if (newS == goal):
                return True
            else:
                return False
        elif (len(s) == 1):
            return False
        else:
            indexes = []

            for i in range(len(s)):
                if (s[i] == goal[i]):
                    newS += s[i]
                else:
                    newS += "_"
                    indexes.append(i)
            
            if (len(indexes) == 2):
                newS = newS.replace("_", s[indexes[1]], 1)
                newS = newS.replace("_", s[indexes[0]])
            elif (len(indexes) == 0):
                for c in s:
                    total = s.count(c)

                    if (total == 2):
                        first = s.find(c)
                        s = s.replace(c, "_", 1)
                        second = s.find(c)

                        temp = newS[second]
                        newS = newS.replace(newS[second], newS[first], 1)
                        newS = newS.replace(newS[first], temp, 1)
                    else:
                        return False

            if (newS == goal):
                return True
            else:
                return False
    
print(Solution().buddyStrings("abcd", "abcd"))
