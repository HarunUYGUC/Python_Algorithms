sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))

if (sayi1 > sayi2):
    tutucu = sayi2
    sayi2 = sayi1
    sayi1 = tutucu

if (sayi1 > sayi3):
    tutucu = sayi3
    sayi3 = sayi1
    sayi1 = tutucu

if (sayi2 > sayi3):
    tutucu = sayi3
    sayi3 = sayi2
    sayi2 = tutucu

print(f"Küçükten büyüğe sıralama: {sayi1} < {sayi2} < {sayi3}")


