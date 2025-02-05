""" https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/ """

class Solution:
    def areAlmostEqual(self, s1, s2):
        if (s1 == s2):
            return True
        else:
            count = 0
            notEquals = []
            newS1 = ""

            for i in range(len(s1)):
                if (s1[i] != s2[i]):
                    count += 1
                    notEquals.append(i)

            if (count > 2) or (count == 1):
                return False
            
            step = 0

            for j in range(len(s1)):
                if (step < 2):
                    if (notEquals[step] == j):
                        newS1 += s2[j]
                        step += 1
                    elif (notEquals[step] != j):
                        newS1 += s1[j]
                else:
                    newS1 += s1[j]

            s1S = []
            for i in notEquals:
                s1S.append(s1[i])
            
            s2S = []
            for i in notEquals:
                s2S.append(s2[i])

            s1S.sort()
            s2S.sort()

            for i in range(len(s1S)):
                if (s1S[i] != s2S[i]):
                    return False
                
            if (newS1 == s2):
                return True
            else:
                return False

print(Solution().areAlmostEqual("caa", "aaz"))
