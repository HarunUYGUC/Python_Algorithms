sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))

if (sayi1 > sayi2):
    tutucu = sayi2
    sayi2 = sayi1
    sayi1 = tutucu

if (sayi1 > sayi3):
    tutucu = sayi3
    sayi3 = sayi1
    sayi1 = tutucu

if (sayi2 > sayi3):
    tutucu = sayi3
    sayi3 = sayi2
    sayi2 = tutucu

print(f"Küçükten büyüğe sıralama: {sayi1} < {sayi2} < {sayi3}")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "1. Sayıyı Giriniz: "
A3: Oku, sayi1
A4: Yaz, "2. Sayıyı Giriniz: "
A5: Oku, sayi2
A6: Yaz, "3. Sayıyı Giriniz: "
A7: Oku, sayi3
A8: Eğer (sayi1 > sayi2) ise
A8.1:   tutucu = sayi2
A8.2:   sayi2 = sayi1
A8.3:   sayi1 = tutucu  
A9: Eğer (sayi1 > sayi3) ise
A9.1:   tutucu = sayi3
A9.2:   sayi3 = sayi1
A9.3:   sayi1 = tutucu
A10: Eğer (sayi2 > sayi3) ise
A10.1:  tutucu = sayi3
A10.2:  sayi3 = sayi2
A10.3:  sayi2 = tutucu
A11: Yaz, "Küçükten büyüğe sıralama: " + sayi1 + "<" + sayi2 + "<" + sayi3
A12: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "1. Sayıyı giriniz: "
GET sayi1
WRITE "2. Sayıyı giriniz: "
GET sayi2
WRITE "3. Sayıyı giriniz: "
GET sayi3
IF (sayi1 > sayi2) THEN
    tutucu = sayi1
    sayi1 = sayi2
    sayi2 = tutucu
ENDIF
IF (sayi1 > sayi3) THEN
    tutucu = sayi1
    sayi1 = sayi3
    sayi3 = tutucu
ENDIF
IF (sayi2 > sayi3) THEN
    tutucu = sayi2
    sayi2 = sayi3
    sayi3 = tutucu
ENDIF
WRITE "Küçükten büyüğe sıralama: " + sayi1 + "<" + sayi2 + "<" + sayi3
"""
