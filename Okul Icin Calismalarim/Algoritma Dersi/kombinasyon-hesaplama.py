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


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Fonksiyon faktoriyel(x)
A2.1:   a = 1
A2.2:   Döngü (b; 1 to (x + 1), adım = 1)
A2.3:       a = a * b
A2.4:   return a
A3: Yaz, "Kombinasyonunu hesaplamak istediğiniz kümenin eleman sayısını giriniz: "
A4: Oku, n
A5: Yaz, "Kaçlı kombinasyonunu hesaplamak istiyorsunuz?: "
A6: Oku, r
A7: f1 = faktoriyel(n)
A8: f2 = faktoriyel(r)
A9: f3 = faktoriyel(n - r)
A10: kombinasyon = f1 / (f2 * f3) 
A11: Yaz, "Kombinasyon: " + kombinasyon
A12: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
FUNCTION faktoriyel(x)
    a = 1
    FOR (b; 1 to (x + 1), STEP = 1)
        a = a * b
    ENDFOR
    return a
ENDFUNCTION
WRITE "Kombinasyonunu hesaplamak istediğiniz kümenin eleman sayısını giriniz: "
GET n
WRITE "Kaçlı kombinasyonunu hesaplamak istiyorsunuz?: "
GET r
f1 = faktoriyel(n)
f2 = faktoriyel(r)
f3 = faktoriyel(n - r)
kombinasyon = f1 / (f2 * f3)
WRITE "Kombinasyon: " + kombinasyon
"""
