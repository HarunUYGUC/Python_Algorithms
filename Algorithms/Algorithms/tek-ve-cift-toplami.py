tekToplami = 0
tekCarpimi = 1
ciftToplami = 0
ciftCarpimi = 1

for i in range(1, 100):
    if (i % 2 == 0):
        ciftToplami += i
        ciftCarpimi *= i
    else:
        tekToplami += i
        tekCarpimi *= i

print(f"Teklerin Toplamı: {tekToplami} \nÇiftlerin Toplamı: {ciftToplami}")
print(f"Teklerin Çarpımı: {tekCarpimi} \nÇiftlerin Çarpımı: {ciftCarpimi}")


# Metinsel olarak gösterilmesi:
"""
A1: Başla.
A2: tekToplami = 0 yap.
A3: tekCarpimi = 1 yap.
A4: ciftToplami = 0 yap.
A5: ciftCarpimi = 1 yap.
A6: 1'den 100'e kadar sırasıyla sayı üreten bir döngü oluştur.
A7: Sırasıyla gelen sayıların 2'ye bölümünden kalan sıfırsa ciftToplami ile o sayıyı topla
ve tekrar ciftToplami na ekle, ciftCarpimi ile o sayıyı çarp ve tekrar ciftCarpimi na ekle.
A8: Sırasıyla gelen sayıların 2'ye bölümünden kalan sıfır değilse tekToplami ile o sayıyı
topla ve tekrar tekToplami na ekle, tekCarpimi ile o sayıyı çarp ve tekrar tekCarpimi na ekle.
A9: Teklerin Toplamı: tekToplami nı yaz.
A10: Çiftlerin Toplamı: ciftToplami nı yaz.
A11: Teklerin Çarpımı: tekCarpimi nı yaz.
A12: Çifterin Çarpımı: ciftCarpimi nı yaz.
A13: Bitir. 
"""

# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: tekToplami = 0 
A3: tekCarpimi = 1
A4: ciftToplami = 0 
A5: ciftCarpimi = 1
A6: Döngü (i; 1 to 100, adım=1)
A6.1:   Eğer (i % 2 == 0) ise
A6.2:       ciftToplami = ciftToplami + i
A6.3:       ciftCarpimi = ciftCarpimi * i
A6.4:   Değil ise
A6.5        tekToplami = tekToplami + i
A6.6:       tekCarpimi = tekCarpimi * i
A7: Yaz, "Teklerin Toplamı: " + tekToplami
A8: Yaz, "Çiftlerin Toplamı: " + ciftToplami
A9: Yaz, "Teklerin Çarpımı: " + tekCarpimi
A10: Yaz, "Çiftlerin Çarpımı: " + ciftCarpimi
A11: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
tekToplami = 0
tekCarpimi = 1
ciftToplami = 0
ciftCarpimi = 1
FOR (i; 1 to 100, STEP = 1)
    IF (i % 2 == 0) THEN
        ciftToplami = ciftToplami + i
        ciftCarpimi = ciftCarpimi * i
    ELSE:
        tekToplami = tekToplami + i
        tekCarpimi = tekCarpimi * i
    ENDIF
ENDFOR
WRITE "Teklerin Toplamı: " + tekToplami
WRITE "Çiftlerin Toplamı: " + ciftToplami
WRITE "Teklerin Çarpımı: " + tekCarpimi
WRITE "Çiftlerin Çarpımı: " + ciftCarpimi
"""
