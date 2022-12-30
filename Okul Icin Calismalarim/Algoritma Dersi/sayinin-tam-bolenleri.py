"""En Hızlı Yöntem"""
# 100.000.000 sayısını anında buluyor.

sayi = int(input("Tam bölenlerini bulmak istediğiniz sayıyı giriniz: "))

sayininTamBolenleri = []

bolen = 1
bolum = sayi

while (bolen < bolum):
    if (sayi % bolen == 0):
        bolum = sayi // bolen
        sayininTamBolenleri.append(bolen)
        sayininTamBolenleri.append(bolum)
    bolen += 1

sayininTamBolenleri.sort()
print(f"Sayının tam bolenleri: {sayininTamBolenleri}")



"""Orta Hızlı Yöntem"""
# 100.000.000 sayısını 7.5 saniyede buluyor.

sayi = int(input("Tam bölenlerini bulmak istediğiniz sayıyı giriniz: "))

sayininTamBolenleri = []

for i in range(1, (sayi + 1)):
    if (sayi % i == 0):
        sayininTamBolenleri.append(i)

print(f"Sayının tam bolenleri: {sayininTamBolenleri}")



"""En Yavaş Yöntem"""
# 100.000.000 sayısını 15.5 saniyede buluyor.

sayi = int(input("Tam bölenlerini bulmak istediğiniz sayıyı giriniz: "))

sayininTamBolenleri = []
sayininTamBolenleri.append(sayi)

for i in range(1, (sayi // 2 + 1)):
    if (sayi % i == 0):
        sayininTamBolenleri.append(i)

sayininTamBolenleri.sort()
print(f"Sayının tam bolenleri: {sayininTamBolenleri}")
