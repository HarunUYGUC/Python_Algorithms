sayi1 = 0
sayi2 = 1
liste = [sayi1, sayi2]

while (len(liste) < 10):
    toplam = sayi1 + sayi2
    liste.append(toplam)
    sayi1 = sayi2
    sayi2 = toplam

print(f"Fibonacci sayı dizisinin ilk 10 elemanı {liste} idir.")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: sayi1 = 0
A3: sayi2 = 1
A4: liste = [sayi1, sayi2]
A5: Döngü (liste eleman sayısı < 10) iken
A5.1:   toplam = sayi1 + sayi2
A5.2:   liste ekle toplam
A5.3:   sayi1 = sayi2
A5.4:   sayi2 = toplam
A6: Yaz, "Fibonacci sayı dizisinin ilk 10 elemanı: " + liste
A7: Bitir
"""
