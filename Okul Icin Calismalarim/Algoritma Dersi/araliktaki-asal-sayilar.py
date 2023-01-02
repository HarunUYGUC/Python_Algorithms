sayi1 = int(input("Hangi aralıktan 'asal sayıları' bulmak istersiniz? Küçük Sayı: "))
sayi2 = int(input("Hangi aralıktan 'asal sayıları' bulmak istersiniz? Büyük Sayı: "))

for i in range(sayi1, (sayi2 + 1)):
    bayrak = True
    for j in range(2, (i // 2 + 1)):
        if (i % j == 0):
            bayrak = False
            break
    if (bayrak == True):
        print(f"Asal Sayı: {i}")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Küçük Sayı: "
A3: Oku, sayi1
A4: Yaz, "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Büyük Sayı: "
A5: Oku, sayi2
A6: Döngü (i; sayi1 to (sayi2 + 1), adım=1) 
A6.1:   bayrak = True
A6.2:   Döngü (j; 2 to (i // 2 + 1), adım=1)
A6.3:       Eğer (i % j == 0) ise
A6.4:           bayrak = False
A6.5:           break
A6.6:   Eğer (bayrak == True) ise
A6.7:       Yaz, "Asal Sayı: " + i
A7: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Küçük Sayı: "
GET sayi1
WRITE "Hangi aralıktan 'asal sayıları' bulmak istersiniz? Büyük Sayı: "
GET sayi2
FOR (i; sayi1 to (sayi2 + 1), STEP = 1)
    bayrak = True
    FOR (j; 2 to (i // 2 + 1), STEP = 1)
        IF (i % j == 0) THEN
            bayrak = False
            break
        ENDIF
    ENDFOR
    IF (bayrak == True) THEN
        WRITE "Asal sayı: " + i
    ENDIF
ENDFOR
"""
