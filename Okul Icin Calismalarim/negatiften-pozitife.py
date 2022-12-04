sayi = float(input("Bir sayı giriniz: "))

if (sayi < 0):
    sayi *= -1

print(f"Sayının pozitif hali = {sayi}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir sayı giriniz: "
A3: Oku, sayi
A4: Eğer (sayi < 0) ise
A5:     sayi = sayi * (-1)
A6: Yaz, sayi
A7: Bitir
"""
