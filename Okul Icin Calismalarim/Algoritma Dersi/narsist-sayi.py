for i in range(999, 99, -1):
    j = 1
    locali = i
    narsistToplam = 0
    while (j <= 3):
        kalan = locali % 10
        narsistToplam += kalan**3
        locali //= 10
        j += 1
    if (narsistToplam == i):
        print(f"{i} sayısı 3 basamaklı en büyük 'narsist sayıdır'.")
        break


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Döngü (i; 999 to 99, adım = -1)
A2.1:   j = 1
A2.2:   locali = i
A2.3:   narsistToplam = 0
A2.4:   Döngü (j <= 3) iken
A2.5:       kalan = locali % 10
A2.6:       narsistToplam = narsistToplam + kalan^3
A2.7:       locali = locali // 10
A2.8:       j = j + 1
A2.9:   Eğer (narsistToplam == i) ise
A2.10:      Yaz, i + " sayısı 3 basamaklı en büyük narsist sayıdır."
A2.11:      break
A3: Bitir
"""
