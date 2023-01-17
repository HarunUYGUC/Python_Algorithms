"""
Klavyeden girilen N değerine göre (N>20), 10-N arası tüm sayıların toplamını, 5-N arası 
tek sayıların tek sayıların çarpımını, 14-N arası çift sayıların toplamını hesaplayıp
yazdıran programın sözde kodunu yazınız ve akış diyagramını çiziniz.
"""

sayi = int(input("Pozitif bir n tam sayısı giriniz: "))

sayininTamBolenleri = []

bolen = 1
bolum = sayi

while (bolen < bolum):
    if (sayi % bolen == 0):
        bolum = sayi // bolen
        if (bolen != bolum):
            sayininTamBolenleri.append(bolen)
            sayininTamBolenleri.append(bolum)
        else:
            sayininTamBolenleri.append(bolen)
    bolen += 1

sayininTamBolenleri.sort()

def faktoriyel(x):
    a = 1
    for b in range(1, (x + 1)):
        a *= b
    return a

faktoriyelToplami = 0

for sayi in sayininTamBolenleri:
    bayrak = True
    for j in range(2, (sayi // 2 + 1)):
        if (sayi % j == 0):
            bayrak = False
            break
    if (bayrak == True):
            faktoriyeli = faktoriyel(sayi)
            faktoriyelToplami = faktoriyelToplami + faktoriyeli

print(f"Koşulları sağlayan faktöriyellerin toplamı {faktoriyelToplami}")


# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Pozitif bir n tam sayısı giriniz: "
GET n
sayininTamBolenleri = []
bolen = 1
bolum = sayi
LOOP (bolen < bolum) THEN
    IF (sayi % bolen == 0) THEN
        bolum = sayi // bolen
        IF (bolen != bolum) THEN
            sayininTamBolenleri append bolen
            sayininTamBolenleri append bolum
        ELSE
            sayininTamBolenleri append bolen
        ENDIF
    bolen = bolen + 1
    ENDIF
ENDLOOP
faktoriyel(x)
    a = 1
    FOR (b; 1 to (x + 1), STEP = 1)
        a = a * b
    ENDFOR
    return a
faktoriyelToplami = 0
FOR (sayi in sayininTamBolenleri)
    bayrak = True
    FOR (j; 2 to (sayi // 2 + 1), STEP = 1)
        IF (sayi % j == 0) THEN
            bayrak = False
            break
        ENDIF
    ENDFOR
    IF (bayrak == True) THEN
        faktoriyeli = faktoriyel(sayi)
        faktoriyelToplami = faktoriyelToplami + faktoriyeli
    ENDIF
ENDFOR
WRITE "Koşulları sağlayan faktöriyellerin toplamı = " + faktoriyelToplami
"""
