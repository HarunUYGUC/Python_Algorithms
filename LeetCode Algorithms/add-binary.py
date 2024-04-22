""" https://leetcode.com/problems/add-binary/description/ """

class Solution:
    def addBinary(self, a, b):
        # a = "0" and b = "0"
        if (a == "0") and (b == "0"):
            return "0"

        # Decimal a
        suma = 0
        lena = len(a) - 1

        for i in range(len(a)):
            if (int(a[i]) == 1):
                suma += 2**lena

            lena -= 1

        # Decimal b
        sumb = 0
        lenb = len(b) - 1

        for i in range(len(b)):
            if (int(b[i]) == 1):
                sumb += 2**lenb
                
            lenb -= 1
        
        # Decimal total
        total = suma + sumb
        binary = "" # Backwards
        newBinary = ""

        while (total > 0):
            binary += str(total % 2)
            total //= 2
        
        for i in range(len(binary) - 1, -1, -1):
            newBinary += binary[i]

        return newBinary
    
solution = Solution()
print(solution.addBinary("1010", "1011"))
