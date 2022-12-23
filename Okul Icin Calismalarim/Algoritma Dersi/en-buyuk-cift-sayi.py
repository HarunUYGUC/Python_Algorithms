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


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Kaç tane pozitif tam sayı gireceksiniz?: "
A3: Oku, kacTane
A4: enBuyuk = -1
A5: Döngü (i; 1 to (kacTane + 1), adım = 1)
A5.1:   Yaz, i + ". sayıyı giriniz: "
A5.2:   Eğer (sayi % 2 == 0) ve (sayi > enBuyuk) ise
A5.3:       enBuyuk = sayi
A6: Eğer (enBuyuk != -1) ise
A6.1:   Yaz, "En buyuk pozitif çift tam sayısı: " + enBuyuk
A7: Değil ise
A7.1:   Yaz, "Pozitif çift tam sayı yoktur."
A8: Bitir
"""
