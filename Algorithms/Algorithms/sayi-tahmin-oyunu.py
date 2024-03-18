import random

bulunacakSayi = random.randint(0, 100)

kacHak = int(input("Kaç hakta 0-100 arsındaki sayıyı bulmak istersiniz?: "))

i = 0
bayrak = False

while (i < kacHak):
    tahmin = int(input("Tahmininizi giriniz: "))
    i += 1
    if (tahmin == bulunacakSayi):
        print(f"Tebrikler, bulunacak sayi {bulunacakSayi} idi.")
        bayrak = True
        break
    elif (tahmin < bulunacakSayi):
        print("Sayınızı arttırınız.")
    else:
        print("Sayınızı azaltınız.")

if (bayrak == False):
    print(f"Bulamadınız! Bulunacak sayi {bulunacakSayi} idi.")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: bulunacakSayi = random(0, 100)
A3: Yaz, "Kaç hakta 0-100 arasındaki sayıyı bulmak istersiniz?: "
A4: Oku, kacHak
A5: i = 0
A6: bayrak = False
A7: Döngü (i < kacHak) iken
A7.1:    Yaz, "Tahmininizi giriniz: "
A7.2:    Oku, tahmin
A7.3:    i = i + 1
A7.4:    Eğer (tahmin == bulunacakSayi) ise
A7.4.1:        Yaz, "Tebrikler, sayıyı buldunuz."
A7.4.2:        bayrak = True
A7.4.3:        break
A7.5:    Değilse (tahmin < bulunacakSayi) ise
A7.5.1:        Yaz, "Sayınızı arttırınız."
A7.6:    Değil ise
A7.6.1:        Yaz, "Sayınızı azaltınız."
A8: Eğer (bayrak == False) ise
A8.1:    Yaz, "Bulamadınız. " + bulunacakSayi + " olacaktı."
A9: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
bulunacakSayi = random(0, 100)
DISPLAY "Kaç hakta 0-100 arasındaki sayıyı bulmak istersiniz?: "
GET kacHak
i = 0
bayrak = False
LOOP (i < kacHak) THEN
    DISPLAY "Tahmininizi giriniz: "
    GET tahmin
    i = i + 1
    IF (tahmin == bulunacakSayi) THEN
        DISPLAY "Tebrikler, sayıyı buldunuz."
        bayrak = True
        break
    ELSEIF (tahmin < bulunacakSayi) THEN
        DISPLAY "Sayınızı arttırınız."
    ELSE
        DISPLAY "Sayınızı azaltınız."
    ENDIF
ENDLOOP
IF (bayrak == False) THEN
    DISPLAY "Bulamadınız. " + bulunacakSayi + " olacaktı."
ENDIF
"""
