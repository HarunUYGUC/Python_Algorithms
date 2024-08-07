""" https://projecteuler.net/problem=2 """

# Method 1 

sayi1 = 0
sayi2 = 1
liste = [sayi1, sayi2]
ciftFibonacciToplamlari = 0

while True:
    fibonacciSayisi = sayi1 + sayi2
    liste.append(fibonacciSayisi)
    sayi1 = sayi2
    sayi2 = fibonacciSayisi
    
    if (liste[len(liste) - 1] > 4000000):
        liste.pop(len(liste) - 1)
        break
    elif (fibonacciSayisi % 2 == 0):
        ciftFibonacciToplamlari += fibonacciSayisi

print(f"4.000.000'den küçük fibonacci sayıları {liste} idir.")
print(f"4.000.000'dan küçük çift fibonacci sayılarının toplamı: {ciftFibonacciToplamlari}")


# Method 2

a = 1
b = 2
sum = b # sum of the even-valued terms

while (b <= 4000000):
    a, b = b, a
    b = a + b

    if (b % 2 == 0):
        sum += b

print(sum)
