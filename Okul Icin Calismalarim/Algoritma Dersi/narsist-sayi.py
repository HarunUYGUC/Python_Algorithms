"""
Narsistik Sayılar (Armstrong Sayılar), n haneli bir sayının basamaklarının n' inci üstlerinin toplamı, 
sayının kendisine eşitse, böyle sayılara narsist sayılar denir. 
Tablodaki gibi 153 sayısı 3 haneli bir narsist sayıdır. 
1^3 + 5^3 + 3^3 = 153 olmaktadır.
"""

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


# "Satır Algoritma" ile gösterilmesi:
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

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
FOR (i; 999 to 99, STEP = -1)
    j = 1
    locali = i
    narsistToplam = 0
    LOOP (j <= 3) THEN
        kalan = locali % 10
        narsistToplam = narsistTopam + kalan
        locali = locali // 10
        j = j + 1
    ENDLOOP
    IF (narsistToplam == i) THEN
        WRITE i + " sayısı 3 basamaklı en büyük narsist sayıdır."
        break
    ENDIF
ENDFOR
"""
