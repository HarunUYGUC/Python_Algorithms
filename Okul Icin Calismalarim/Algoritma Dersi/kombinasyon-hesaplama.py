def faktoriyel(x):
    a = 1
    for b in range(1, (x + 1)):
        a *= b
    return a

n = int(input("Kombinasyonunu hesaplamak istediğiniz kümenin eleman sayısını giriniz: "))
r = int(input("Kaçlı kombinasyonunu hesaplamak istiyorsunuz?: "))

f1 = faktoriyel(n)
f2 = faktoriyel(r)
f3 = faktoriyel(n - r)

kombinasyon = f1 / (f2 * f3)

print(f"{n} elemanlı kümenin {r}'lü kombinasyonlarının sayısı: {int(kombinasyon)}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Fonksiyon faktoriyel(x)
A2.1:   a = 1
A2.2:   Döngü (b; 1 to (x + 1), adım = 1)
A2.3:       a = a * b
A2.4:   return a
A3: f1 = faktoriyel(n)
A4: f2 = faktoriyel(r)
A5: f3 = faktoriyel(n - r)
A6: kombinasyon = f1 / (f2 * f3) 
A7: Yaz, "Kombinasyon: " + kombinasyon
A8: Bitir
"""
