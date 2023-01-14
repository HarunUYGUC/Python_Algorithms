sayi1 = int(input("EBOB'unu bulacağınız birinci sayıyı giriniz: "))
sayi2 = int(input("EBOB'unu bulacağınız ikinci sayıyı giriniz: "))

if (sayi1 > sayi2):
    kucukSayi = sayi2
else:
    kucukSayi = sayi1

for i in range(kucukSayi, 0, -1):
    if (sayi1 % i == 0) and (sayi2 % i == 0):
        ebob = i
        break

print(f"EBOB: {ebob}")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "EBOB'unu bulacağınız birinci sayıyı giriniz: "
A3: Oku, sayi1
A4: Yaz, "EBOB'unu bulacağınız ikinci sayıyı giriniz: "
A5: Oku, sayi2
A6: Eğer (sayi1 > sayi2) ise
A6.1:   kucukSayi = sayi2
A7: Değil ise
A7.1:   kucukSayi = sayi1
A8: Döngü (i; kucukSayi to 0, adım=-1)
A8.1:   Eğer (sayi1 % i == 0) ve (sayi2 % i == 0) ise
A8.2:       ebob = i
A8.3:       break
A9: Yaz, "EBOB: " + ebob
A10: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "EBOB'unu bulacağınız birinci sayıyı giriniz: "
GET sayi1
WRITE "EBOB'unu bulacağınız ikinci sayıyı giriniz: "
GET sayi2
IF (sayi1 > sayi2) THEN
    kucukSayi = sayi2
ELSE
    kucukSayi = sayi1
ENDIF
FOR (i; kucukSayi to 0, STEP = -1)
    IF (sayi1 % 2 == 0) and (sayi2 % i == 0) THEN
        ebob = i
        break
    ENDIF
ENDFOR
WRITE "EBOB: " + ebob
"""
