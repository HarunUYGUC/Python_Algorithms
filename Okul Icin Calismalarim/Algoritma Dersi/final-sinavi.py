# Aklımda kaldığı kadarıyla sınav soruları ve çözümlerim böyleydi!!! 
# Sınavda yazdığım algoritmaların Python kodunu yazarak deneyeceğim.

"""
--1. Soru
Kullanıcıdan bir tam sayı girmesini isteyiniz. Eğer sayı pozitif ise sayının tam bölenlerinden 
asal olanların 7'ye tam bölünenlerini ekrana yazdırınız. Eğer sayı pozitif değilse pozitif değil yazdırınız.
"""


"""
--2. Soru
Kullanıcıdan pozitif bir tam sayı girmesini isteyiniz ve sayıyı aşağıdaki şekilde gösteriniz.
12345 şeklinde girilen sayıyı 5 x 10^0 + 4 x 10^1 + 3 x 10^2 + 2 x 10^3 + 1 x 10^4 şeklinde yazan 
algoritmayı yazınız.
"""

# Sınavda yaptığım yöntem: 
"""Alt alta yazmak için böyle yaptım."""

sayi = int(input("Pozitif bir tam sayı giriniz: "))

n = 0

while (sayi >= 10):
    basamak = sayi % 10
    sayi //= 10
    gosterim = f"{basamak} x 10^{n} x"
    print(f"{10**n}'ler basamağı: {gosterim}")
    n += 1

gosterim = f"{sayi} x 10^{n}"
print(f"{10**n}'ler basamağı: {gosterim}")


# 2. Yöntem:
"""Normalde böyle yapardım."""

sayi = int(input("Pozitif bir tam sayı giriniz: "))

n = 0
liste = []

while (sayi >= 10):
    basamak = sayi % 10
    sayi //= 10
    gosterim = f"{basamak} x 10^{n} x "
    liste.append(gosterim)
    n += 1

gosterim = f"{sayi} x 10^{n}"
liste.append(gosterim)

print(f"Gösterim: {liste}")


"""
--3. Soru
Kullanıcıdan pozitif bir tam sayı girmesini isteyin. Girilen sayının permütasyonunu hesaplayıp 
asal sayı olup olmadığına göre çıktı veren algoritmayı yazınız.
"""
