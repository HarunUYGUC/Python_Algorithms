sayi = float(input("Yüzdesini hesaplamak istediğiniz sayıyı giriniz: "))
yuzdesi = float(input("Yüzde kaç?: "))

sonuc = sayi * yuzdesi / 100

print(f"{sayi} sayısının %{yuzdesi}'i: {sonuc}")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Yüzdesini hesaplamak istediğiniz sayıyı giriniz: "
A3: Oku, sayi
A4: Yaz, "Yüzde kaç?: "
A5: Oku, yuzdesi
A6: sonuc = sayi * yuzdesi / 100
A7: Yaz, "Cevap: " + sonuc
A8: Bitir
"""
