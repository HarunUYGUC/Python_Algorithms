class Solution:
    def reverseBits(self, n):
        # :032b baştaki sıfırları korur (32 bit olacak şekilde). :b ise siliyordu.
        binary = f"{n:032b}" # Tam sayıyı ikiliğe çevirir.
        reverse = binary[::-1] # String'in tersini alır.
        return int(reverse, 2) # 2'lik tabandaki sayıyı 10'luk tabana çevirir.
