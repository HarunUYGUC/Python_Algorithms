birler_basamagi = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar_basamagi = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

def okunus(sayi):
    birler = sayi % 10
    onlar = sayi // 10

    return onlar_basamagi[onlar] + " " + birler_basamagi[birler]

sayi = int(input("Sayı Giriniz: "))

print(okunus(sayi))
