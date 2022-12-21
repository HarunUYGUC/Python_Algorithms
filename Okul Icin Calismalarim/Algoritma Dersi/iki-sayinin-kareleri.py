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


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Pozitif bir tam sayı giriniz: "
A3: Oku, sayi
A4: bayrak = False
A5: i = 0
A6: j = 0
A7: Döngü (i <= sayi) iken
A7.1:   i = i + 1
A7.2:   j = 0
A7.3:       Döngü (j <= sayi) iken
A7.4:           j = j + 1
A7.5:           Eğer (i^2 + j^2 == sayi) ise
A7.6:               Yaz, i + "'nin ve " + j + "'nin karesinin toplamı = " + sayi
A7.7:               bayrak = True
A7.8:               i = sayi + 1
A7.9:               break
A8: Eğer (bayrak == False) ise
A8.1:   Yaz, sayi + " iki sayının karesinin toplamı şeklinde yazılamaz."
A9: Bitir 
"""
