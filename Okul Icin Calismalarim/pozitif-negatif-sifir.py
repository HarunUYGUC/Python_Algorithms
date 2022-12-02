x = int(input("Bir sayı giriniz: "))

if (x > 0):
    print(f"{x} sayısı pozitif bir sayıdır.")
elif (x == 0):
    print(f"{x} sayısı 0 (sıfırdır).")
else:
    print(f"{x} sayısı negatif bir sayıdır.")


# Satır algoritma ile gösterilmesi:
"""
A1: Başla.
A2: Bir sayı (x) giriniz
A3: Eğer x sayısı sıfırdan büyükse "pozitif" yaz.
A4: Eğer x sayısı sıfırdan küçükse "negatif" yaz.
A5: Eğer x sayısı sıfıra eşitse "sıfır" yaz.
A6: Bitir.
"""

# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir sayı giriniz: "
A3: Oku, x
A4: Eğer (x > 0) ise
A4.1:   Yaz, "Pozitif"
A5: Eğer (x < 0) ise
A5.1:   Yaz, "Negatif"
A6: Eğer (x == 0) ise
A6.1:   Yaz, "Sıfır"
A7: Bitir
"""
