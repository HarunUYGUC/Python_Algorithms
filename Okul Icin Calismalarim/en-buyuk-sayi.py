# Yöntem 1:

sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))

if (sayi1 > sayi2):
    tutucu = sayi1
    sayi1 = sayi2
    sayi2 = tutucu
if (sayi2 > sayi3):
    tutucu = sayi2
    sayi2 = sayi3
    sayi3 = tutucu

print(f"En büyük sayı: {sayi3}")


# Yöntem 2: 
"""Bu yöntem daha mantıklı bir yöntem."""

sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))

if (sayi1 > sayi2) and (sayi1 > sayi3):
    enBuyukSayi = sayi1
elif (sayi2 > sayi3) and (sayi2 > sayi1):
    enBuyukSayi = sayi2
else:
    enBuyukSayi = sayi3

print(f"En büyük sayı: {enBuyukSayi}")


# Satır algoritma ile gösterilmesi:
"""
A1: Başla.
A2: 1. Sayıyı giriniz.
A3: 2. Sayıyı giriniz.
A4: 3. Sayıyı giriniz.
A5: Eğer 1. sayı hem 2. sayıdan hem de 3. sayıdan büyükse "1. sayı en büyük sayıdır." yaz.
A6: Eğer 2. sayı hem 1. sayıdan hem de 3. sayıdan büyükse "2. sayı en büyük sayıdır." yaz.
A7: Eğer 3. sayı hem 1. sayıdan hem de 2. sayıdan büyükse "3. sayı en büyük sayıdır." yaz.
A8: Bitir.
"""

# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz "1. Sayıyı (sayi1) giriniz: "
A3: Oku sayi1
A4: Yaz "2. Sayıyı (sayi2) giriniz: "
A5: Oku sayi2
A6: Yaz "3. Sayıyı (sayi3) giriniz: "
A7: Oku sayi3
A8: Eğer (sayi1 > sayi2) ve (sayi1 > sayi3) ise
A8.1:   enBuyukSayi = sayi1
A9: Eğer (sayi2 > sayi3) ve (sayi2 > sayi1) ise
A9.1:   enBuyukSayi = sayi2
A10: Eğer (sayi3 > sayi1) ve (sayi3 > sayi2) ise
A10.1:  enBuyukSayi = sayi3
A11: Yaz enBuyukSayi
A12: Bitir.
"""
