"""  

sin(x) = x - (x^2 / 2!) + (x^4 / 4!) - (x^6 / 6!) ...
şeklinde giden denklemin ilk 10 teriminin sonucunu hesaplayınız.

"""

def faktoriyel(x):
    fak = 1

    for i in range(1, x + 1):
        fak *= i

    return fak

x = int(input("Radyan cinsinden bir sayı giriniz: "))

adet = 1 # x var.
sonuc = x
sayi = 2 # us ve faktoriyel hesabı için

while (adet < 10):
    adet += 1

    if (adet % 2 == 0):
        sonuc += - x**sayi / faktoriyel(sayi)
    else:
        sonuc += x**sayi / faktoriyel(sayi)

    sayi += 2

print(f"Sonuç = {sonuc}")
