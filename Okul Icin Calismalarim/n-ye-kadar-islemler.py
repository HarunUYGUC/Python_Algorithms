x = int(input("Bir sayı giriniz: "))

tekToplami = 0
tekCarpimi = 1
ciftlerinKareleriToplami = 0

for i in range(1, x+1):
    if (i % 2 == 0):
        ciftinKaresi = i**2
        ciftlerinKareleriToplami += ciftinKaresi
    else:
        tekToplami += i
        tekCarpimi *= i

print(f"Teklerin Toplamı: {tekToplami} \nTeklerin Çarpımı: {tekCarpimi}")
print(f"Çiflerin Karelerinin Toplamı: {ciftlerinKareleriToplami}")
