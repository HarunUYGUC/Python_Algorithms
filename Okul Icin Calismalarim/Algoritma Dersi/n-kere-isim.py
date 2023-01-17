isim = input("Bir isim giriniz: ")
kacKere = int(input("İsminizi kaç kere alt alta yazdırmak istersiniz: "))

i = 1
while (i <= kacKere):
    print(f"{i}. {isim}")
    i += 1


# "Satır Algoritma" ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Bir isim giriniz."
A3: Oku, isim
A4: Yaz, "Kaç kere ismi yazdırmak istersiniz?"
A5: Oku, kacKere
A6: i = 1
A7: Döngü (i <= kacKere) ise
A7.1:   Yaz, i + "." + isim
A7.2:   i = i + 1
A8: Bitir
"""

# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
WRITE "Bir isim giriniz: "
GET isim
WRITE "İsminizi kaç kere alt alta yazdırmak istersiniz?: "
GET kacKere
i = 1
LOOP (i <= kacKere) THEN
    WRITE i + "." + isim
    i = i + 1
ENDLOOP
"""
