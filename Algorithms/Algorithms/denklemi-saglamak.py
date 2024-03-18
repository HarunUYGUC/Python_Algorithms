b = int(input("Bir tam sayı giriniz: "))

bayrak = False

for a in range(1, 100):
    if (a**3 - a**2 == b):
        print(f"b = {b} iken a = {a} sayısı 'a^3 - a^2 = b' denklemini sağlar.")
        bayrak = True
        break

if (bayrak == False):
    print(f"b = {b} sayısı iken 'a^3 - a^2 = b' denklemini sağlayan bir 0 < a < 100 değeri yoktur.")


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir tam sayı giriniz: "
A3: Oku, b
A4: bayrak = False
A5: Döngü (a; 1 to 100, adım = 1)
A5.1:   Eğer (a^3 - a^2 == b) ise
A5.2:       Yaz, a + " sayısı bu denklemi sağlar."
A5.3:       bayrak = True
A5.4:       break
A6: Eğer (bayrak == False) ise
A6.1:   Yaz, "Bu denklemi sağlayan bir a sayısı yoktur."
A7: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Bir tam sayı giriniz: "
GET b
bayrak = False
FOR (a; 1 to 100, STEP = 1)
    IF (a^3 - a^2 == b) THEN
        WRITE a + " sayısı (a^3 - a^2 = b) denklemini sağlar."
        bayrak = True
        break
    ENDIF
ENDFOR
IF (bayrak == False) THEN
    WRITE "(a^3 - a^2 = b) denklemini sağlayan bir 0 < a < 100 sayısı yoktur."
ENDIF
"""
