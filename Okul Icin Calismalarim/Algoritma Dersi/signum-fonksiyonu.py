x = float(input("f(x) = x^2 - 5x + 3 fonksiyonu için bir x sayısı giriniz ve fonksiyonun o noktadaki işaretini öğreniniz: "))
y = x**2 - 5*x + 3

if (y < 0):
    print(f"{x} sayısı için f(x) fonksiyonunun işareti '-1'dir.")
elif (y == 0):
    print(f"{x} sayısı için f(x) fonksiyonunun işareti '0'dır.")
elif (y > 0):
    print(f"{x} sayısı için f(x) fonksiyonunun işareti '1'dir.")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir sayı giriniz: "
A3: Oku, x
A4: y = x^2 - 5*x + 3
A5: Eğer (y < 0) ise
A5.1:   Yaz, "Fonksiyonun işareti -1'dir."
A5.2: Eğer değilse (y == 0) ise
A5.3:   Yaz, "Fonksiyonun işareti 0'dır."
A5.4: Eğer değilse (y > 0) ise
A5.5:   Yaz, "Fonksiyonun işareti 1'dir."
A6: Bitir
"""
