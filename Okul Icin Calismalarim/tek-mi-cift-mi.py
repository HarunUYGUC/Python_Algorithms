x = int(input("Pozitif bir tam sayı giriniz: "))

if (x % 2 == 0):
    print(f"{x} sayısı pozitif bir çift sayıdır.")
else:
    print(f"{x} sayısı pozitif bir tek sayıdır.")


# Satır algoritma ile gösterilmesi:
"""
A1: Başla.
A2: Pozitif bir tam sayı (x) giriniz
A3: Sayının 2'ye bölümünden kalan sıfırsa "Pozitif bir çift sayıdır." yaz.
A4: Sayının 2'ye bölümünden kalan sıfır değilse "Pozitif bir tek sayıdır." yaz.
A5: Bitir.
"""

# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz "Bir sayı (x) giriniz: "
A3: Oku x
A4: Eğer (x % 2 == 0) ise
A4.1:   Yaz "Pozitif bir çift sayıdır."
A5: Değil ise
A5.1:   Yaz "Pozitif bir tek sayıdır."
A6: Bitir
"""
