kacTane = int(input("Kaç tane pozitif tam sayı gireceksiniz?: "))

enBuyuk = -1

for i in range(1, (kacTane + 1)):
    sayi = int(input(f"{i}. sayıyı giriniz: "))
    if (sayi % 2 == 0) and (sayi > enBuyuk):
        enBuyuk = sayi

if (enBuyuk != -1):
    print(f"Girilen sayılar arasındaki en büyük pozitif çift tam sayısı {enBuyuk} idir.")
else:
    print(f"Girilen sayılar arasında pozitif çift tam sayı yoktur.")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Kaç tane pozitif tam sayı gireceksiniz?: "
A3: Oku, kacTane
A4: enBuyuk = -1
A5: Döngü (i; 1 to (kacTane + 1), adım = 1)
A5.1:   Yaz, i + ". sayıyı giriniz: "
A5.2:   Oku, sayi
A5.3:   Eğer (sayi % 2 == 0) ve (sayi > enBuyuk) ise
A5.4:       enBuyuk = sayi
A6: Eğer (enBuyuk != -1) ise
A6.1:   Yaz, "En buyuk pozitif çift tam sayısı: " + enBuyuk
A7: Değil ise
A7.1:   Yaz, "Pozitif çift tam sayı yoktur."
A8: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Kaç tane pozitif tam sayı gireceksiniz?: "
GET kacTane
enBuyuk = -1
FOR (i; 1 to (kacTane + 1), STEP = 1)
    WRITE i + ". sayıyı giriniz: "
    GET sayi
    IF (sayi % 2 == 0) and (sayi > enBuyuk) THEN
        enBuyuk = sayi
    ENDIF
ENDFOR
IF (enBuyuk != -1) THEN
    WRITE "En buyuk pozitif çift tam sayısı: " + enBuyuk
ELSE
    WRITE "Pozitif çift tam sayı yoktur."
ENDIF
"""
