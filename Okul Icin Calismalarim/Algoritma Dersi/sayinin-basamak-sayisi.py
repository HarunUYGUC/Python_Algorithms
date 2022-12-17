sayi = int(input("Pozitif bir tam sayı giriniz: "))

n = 0

while True:
    if (sayi >= 10**n) and (sayi < 10**(n + 1)):
        print(f"{sayi}, {n + 1} basamaklı.")
        break
    else:
        n += 1


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Pozitif bir tam sayı giriniz: "
A3: Oku, sayi
A4: n = 0
A5: Döngü (True) iken
A5.1:   Eğer (sayi >= 10**n) ve (sayi < 10**(n + 1)) ise
A5.2:       Yaz, n + 1 + " basamaklı."
A5.3        break
A5.4:   Değil ise
A5.5:       n = n + 1
A6: Bitir
"""
