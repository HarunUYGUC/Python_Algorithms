"1-100 arasıda haneleri toplamı tek olan tam sayıların listesini veren program."

liste = []

for i in range(1, 100):
    toplam = (i % 10) + int(i / 10)
    if (toplam % 2 == 1):
        liste.append(i)

print(f"Haneleri toplamı tek olan sayılar: {liste}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: liste
A3: Döngü (i; 1 to 100, adım=1)
A3.1:   toplam = (i % 10) + int(i / 10)
A3.2:   Eğer (toplam % 2 == 1) ise
A3.3:       i ekle liste
A4: Yaz, liste
A5: Bitir
"""
