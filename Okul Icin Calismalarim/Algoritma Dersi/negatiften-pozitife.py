sayi = float(input("Bir sayı giriniz: "))

if (sayi < 0):
    sayi *= -1

print(f"Sayının pozitif hali = {sayi}")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir sayı giriniz: "
A3: Oku, sayi
A4: Eğer (sayi < 0) ise
A5:     sayi = sayi * (-1)
A6: Yaz, "Sayının pozitif hali: " + sayi
A7: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Bir sayı giriniz: "
GET sayi
IF (sayi < 0) THEN
    sayi = sayi * (-1)
ENDIF
WRITE "Sayının pozitif hali: " + sayi
"""
