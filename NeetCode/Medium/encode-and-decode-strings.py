class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded

    def decode(self, s):
        decoded = []
        i = 0

        while (i  < len(s)):
            j = i

            while (s[j] != "#"):
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length
            decoded.append(s[start:end])

            i = end
        
        return decoded

solution = Solution()
strs = ["neet","code","love","you"]
print(solution.encode(strs))
print(solution.decode(solution.encode(strs)))
