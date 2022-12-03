sayi1 = int(input("EKOK'unu bulacağınız 1. sayıyı giriniz: "))
sayi2 = int(input("EKOK'unu bulacağınız 2. sayıyı giriniz: "))

asalSayilar = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
ekok = 1

for i in asalSayilar:
    while (sayi1 % i == 0) or (sayi2 % i == 0):
        if (sayi1 % i == 0) and (sayi2 % i == 0):
            sayi1 /= i
            sayi2 /= i
            ekok *= i
        elif (sayi1 % i == 0):
            sayi1 /= i
            ekok *= i
        elif (sayi2 % i == 0):
            sayi2 /= i
            ekok *= i

print(f"EKOK: {ekok}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "1. Sayıyı Giriniz: "
A3: Oku, sayi1
A4: Yaz, "2. Sayıyı Giriniz: "
A5: Oku, sayi2
A6: asalSayilar = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
A7: ekok = 1
A8: Döngü (i in asalSayilar)
A8.1:   Döngü (sayi1 % i == 0) veya (sayi2 % i == 0) ise
A8.2:       Eğer (sayi1 % i == 0) ve (sayi2 % i == 0) ise
A8.3:           sayi1 = sayi1 / i
A8.4:           sayi2 = sayi2 / i
A8.5:           ekok = ekok * i
A8.6:       Eğer değilse (sayi1 % i == 0) ise
A8.7:           sayi1 = sayi1 / i
A8.8:           ekok = ekok * i
A8.9:       Eğer değilse (sayi2 % i == 0) ise
A8.10:          sayi2 = sayi2 / i
A8.11:          ekok = ekok * i
A9: Yaz, ekok
A10: Bitir
"""
