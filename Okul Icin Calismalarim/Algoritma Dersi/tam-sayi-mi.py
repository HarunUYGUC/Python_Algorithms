sayi = float(input("Bir sayı giriniz: "))

if (sayi % 2 == 0) or (sayi % 2 == 1):
    print(f"{sayi} sayısı bir tam sayıdır.")
else:
    print(f"{sayi} sayısı tam sayı değildir.")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir sayı giriniz: "
A3: Oku, sayi
A4: Eğer (sayi % 2 == 0) veya (sayi % 2 == 1) ise
A4.1:   Yaz, "Girilen sayı bir tam sayıdır."
A5: Değil ise
A5.1:   Yaz, "Girilen sayı tam sayı değildir."
A6: Bitir
"""
