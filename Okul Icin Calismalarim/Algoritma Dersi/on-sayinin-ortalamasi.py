toplam = 0
for i in range(1, 11):
    sayi = float(input(f"{i}. sayıyı giriniz: "))
    toplam += sayi

ortalama = toplam / 10
print(f"Sayıların Toplamı = {toplam} | Ortalaması = {ortalama}")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: toplam = 0
A3: Döngü (i; 1 to 10, adım=1)
A3.1:   Yaz, i + ". sayıyı giriniz: "
A3.2:   Oku, sayi
A3.3:   toplam = toplam + sayi
A4: ortalama = toplam / 10
A5: Yaz, "Sayıların ortalaması: " + ortalama
A6: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
toplam = 0
FOR (i; 1 to 11, STEP = 1)
    WRITE i + ". Sayıyı Giriniz: "
    GET sayi
    toplam = toplam + sayi
ENDFOR
ortalama = toplam / 10
WRITE "Sayıların ortalaması: " + ortalama
"""
