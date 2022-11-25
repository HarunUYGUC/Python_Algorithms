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

