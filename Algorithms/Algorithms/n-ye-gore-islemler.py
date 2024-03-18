n = int(input("20'den büyük bir n sayısı giriniz: "))

toplam = 0

for i in range(10, (n + 1)):
    toplam += i

print(f"10 - n: {n} arası sayıların toplamı = {toplam}")


teklerinCarpimi = 1

for i in range(5, (n + 1)):
    if (i % 2 == 1):
        teklerinCarpimi *= i

print(f"5 - n: {n} arası tek sayıların çarpımı = {teklerinCarpimi}")


ciftlerinToplami = 0

for i in range(14, n):
    if (i % 2 == 0):
        ciftlerinToplami += i

print(f"14 - n: {n} arası çift sayıların toplamı = {ciftlerinToplami}")

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "20'den büyük bir n sayısı giriniz: "
GET n
toplam = 0
FOR (i; 10 to (n + 1), STEP = 1)
    toplam = toplam + i
ENDFOR
WRITE "10-n: " + n + " arası sayıların toplamı = " + toplam
teklerinCarpimi = 1
FOR (i; 5 to (n + 1), STEP = 1)
    IF (i % 2 == 1) THEN
        teklerinCarpimi = teklerinCarpimi * i
    ENDIF
ENDFOR
WRITE "5-n: " + n + " arası tek sayıların çarpımı = " + teklerinCarpimi
ciftlerinToplami = 0
FOR (i; 14 to (n + 1), STEP = 1)
    IF (i % 2 == 0) THEN
        ciftlerinToplami = ciftlerinToplami + i
    ENDIF
ENDFOR
WRITE "14-n: " + n + " arası çift sayıların toplamı = " + ciftlerinToplami
"""
