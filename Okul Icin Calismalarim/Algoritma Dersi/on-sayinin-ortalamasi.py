toplam = 0
for i in range(1, 11):
    sayi = float(input(f"{i}. sayıyı giriniz: "))
    toplam += sayi

ortalama = toplam / 10
print(f"Sayıların Toplamı = {toplam} | Ortalaması = {ortalama}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: toplam = 0
A3: Döngü (i; 1 to 10, adım=1)
A3.1:   Yaz, i + ". sayıyı giriniz: "
A3.2:   Oku, sayi
A3.3:   toplam = toplam + sayi
A4: ortalama = toplam / 10
A5: Yaz, ortalama
A6: Bitir
"""
