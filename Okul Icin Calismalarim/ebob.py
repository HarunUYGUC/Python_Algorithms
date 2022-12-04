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


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "1. Sayıyı Giriniz: "
A3: Oku, sayi1
A4: Yaz, "2. Sayıyı Giriniz: "
A5: Oku, sayi2
A6: Eğer (sayi1 > sayi2) ise
A6.1:   kucukSayi = sayi2
A7: Değil ise
A7.1:   kucukSayi = sayi1
A8: Döngü (i; kucukSayi to 0, adım=-1)
A8.1:   Eğer (sayi1 % i == 0) ve (sayi2 % i == 0) ise
A8.2:       ebob = i
A8.3:       break
A9: Yaz, ebob
A10: Bitir
"""
