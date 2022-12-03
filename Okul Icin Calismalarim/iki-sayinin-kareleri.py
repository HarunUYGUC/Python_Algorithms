sayi = int(input("Pozitif bir tam sayı giriniz: "))

bayrak = False
i = 0
j = 0

while (i <= sayi):
    i += 1
    j = 0
    while (j <= sayi):
        j += 1
        if (i**2 + j**2 == sayi):
            print(f"{i}'nin karesi ve {j}'nin karesinin toplamı = {sayi}")
            bayrak = True
            i = sayi + 1
            break

if (bayrak == False):
    print(f"{sayi}, iki sayının karesinin toplamı şeklinde yazılamaz.")
