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
        break
    elif (fibonacciSayisi % 2 == 0):
        ciftFibonacciToplamlari += fibonacciSayisi

liste.pop(len(liste) - 1)
print(f"400'den küçük fibonacci sayıları {liste} idir.")
print(f"Çift fibonacci sayılarının toplamı: {ciftFibonacciToplamlari}")