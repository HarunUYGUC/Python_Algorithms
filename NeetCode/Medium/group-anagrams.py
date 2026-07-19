class Solution:    
    def findLetters(self, st):
        dict1 = {}

        for c in st:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1

        return dict1

    def groupAnagrams(self, strs):
        words = []

        for st in strs:
            words.append((st, self.findLetters(st)))
        
        result = []
        used = [False] * len(words) # Bu kelimeyi daha önce bir gruba ekledim mi?
        # used = [False, False, False, False, False, False]

        for i in range(len(words)):
            if used[i]:
                continue

            group = [words[i][0]]
            used[i] = True

            for j in range(i + 1, len(words)):
                if not used[j] and words[i][1] == words[j][1]:
                    group.append(words[j][0])
                    used[j] = True

            result.append(group)

        return result


solution = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(solution.groupAnagrams(strs))
