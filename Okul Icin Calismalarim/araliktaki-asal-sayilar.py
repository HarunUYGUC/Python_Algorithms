sayi1 = int(input("Hangi aralıktan 'asal sayıları' bulmak istersiniz? Küçük Sayı: "))
sayi2 = int(input("Hangi aralıktan 'asal sayıları' bulmak istersiniz? Büyük Sayı: "))

for i in range(2, (sayi2 + 1)):
    bayrak = True
    for j in range(2, (i // 2 + 1)):
        if (i % j == 0):
            bayrak = False
    if (bayrak == True):
        print(f"Asal Sayı: {i}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Küçük Sayı: "
A3: Oku, sayi1
A4: Yaz, "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Büyük Sayı: "
A5: Oku, sayi2
A6: Döngü (i; 2 to (sayi2 + 1), adım=1) 
A6.1:   bayrak = True
A6.2:   Döngü (j; 2 to (i // 2 + 1), adım=1)
A6.3:       Eğer (i % j == 0) ise
A6.4:           bayrak = False
A6.5:   if (bayrak = True) ise
A6.6:       Yaz, "Asal Sayı: " + i
A7: Bitir
"""
