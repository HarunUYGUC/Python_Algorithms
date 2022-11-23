# EBOB'u bulduktan sonra EBOB yardımıyla EKOK bulan program. 
# https://jn7.net/girilen-iki-sayinin-asal-bolenlerini-ekok-bulma/

sayi1 = int(input("Birinci Sayıyı Giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))
if (sayi1>sayi2):
    kucuksayi = sayi2
else:
    kucuksayi = sayi1
for i in range(1,kucuksayi+1):
    if (sayi1 % i==0) and (sayi2%i ==0):
        ebob = i
print("Ebob = ",ebob)
print("Ekok = ", (sayi1*sayi2)//ebob)


# Asal sayıları bularak EKOK bulmak.
# https://jn7.net/girilen-iki-sayinin-asal-bolenlerini-ekok-bulma/

"""Asal sayıları bulmak için gerekli olan kod kısmının başlangıcı."""
def asal(a):
    if a == 1 :
        return False
    elif a == 2 or a==3 or a==5 or a==7: #Daha az işlemle asal sayıyı bulmak için belli sayıları True döndürüyoruz
        return True
    elif a%2== 0 or a%3==0 or a%5==0 or a%7==0: #İşlemleri hafifletmek için tüm çift sayıları, 3,5 ve 7 nin katlarını False döndürüyoruz
        return False
    else:
        for i in range(3,a): #3 ten başlayarak sayının kendisine kadar olan tüm sayılara bölünüp bölünmediğini kontrol ediyoruz.
            if a%i==0:
                return False
    return True
"""Asal sayıları bulmak için gerekli olan kod kısmının başlangıcı."""
"""EKOK bulmak için gerekli olan kod kısmının başlangıcı."""
sayi1 = int(input("Birinci Sayıyı Giriniz")) #ekok bulmak için iki sayı girmesini istiyoruz.
sayi2 = int(input("İkinci Sayıyı Giriniz"))
bolenler = []
if sayi1 > sayi2: #Döngüyü büyük olan sayıya kadar yapabilmek için girilen sayılardan büyük olanı buluyoruz.
    buyuksayi = sayi1
else:
    buyuksayi = sayi2
i=1
while i<=buyuksayi: #Bölenleri bulmak için büyük sayıya kadar bir döngü oluşturduk
    i+=1
    if asal(i):
        if (sayi1 % i == 0) and (sayi2 % i==0):
            bolenler.append(i)
            sayi1= sayi1//i
            sayi2= sayi2//i
            i=1 #saylar i sayısına bölünürse tekrar döngüyü 1 den başlatacağız.
        elif sayi1 % i ==0:
            bolenler.append(i)
            sayi1= sayi1//i
            i=1
        elif sayi2 % i ==0:
            bolenler.append(i)
            sayi2= sayi2//i
            i=1
print(bolenler)
ekok=1
for i in bolenler:
    ekok = ekok * i 
print(sayi1, "ve", sayi2, "sayılarının EKOK'u = ", ekok)
"""EKOK bulmak için gerekli olan kod kısmının bitişi."""
