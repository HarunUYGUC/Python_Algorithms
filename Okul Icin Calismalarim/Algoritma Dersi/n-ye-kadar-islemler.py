x = int(input("Bir sayı giriniz: "))

tekToplami = 0
tekCarpimi = 1
ciftlerinKareleriToplami = 0

for i in range(1, (x + 1)):
    if (i % 2 == 0):
        ciftinKaresi = i**2
        ciftlerinKareleriToplami += ciftinKaresi
    else:
        tekToplami += i
        tekCarpimi *= i

print(f"{x}'e Kadar Ki Teklerin Toplamı: {tekToplami} \nTeklerin Çarpımı: {tekCarpimi}")
print(f"{x}'e Kadar Ki Çiflerin Karelerinin Toplamı: {ciftlerinKareleriToplami}")


# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Bir sayı giriniz: "
GET sayi
tekToplami = 0
tekCarpimi = 1
ciftlerinKareleriToplami = 0
FOR (i; 1 to (sayi + 1), STEP = 1)
    IF (i % 2 == 0) THEN
        ciftinKaresi = i^2
        ciftlerinKareleriToplami = ciftlerinKareleriToplami + ciftinKaresi
    ELSE
        tekToplami = tekToplami + i
        tekCarpimi = tekCarpimi * i
    ENDIF
ENDFOR
WRITE sayi + "'e Kadar Ki Teklerin Toplamı: " + tekToplami
WRITE sayi + "'e Kadar Ki Teklerin Çarpımı: " + tekCarpimi
WRITE sayi + "'e Kadar Ki Çiftlerin Kareleri Toplamı: " + ciftlerinKareleriToplami
"""
