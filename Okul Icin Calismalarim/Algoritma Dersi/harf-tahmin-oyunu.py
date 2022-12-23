import random
import string

bulunacakHarf = random.choice(string.ascii_uppercase)

kacHak = int(input("Kaç hakta büyük harfi bulmak istersiniz?: "))

i = 0
bayrak = False

while (i < kacHak):
    tahmin = input("Tahmininizi giriniz: ")
    i += 1
    if (tahmin == bulunacakHarf):
        print(f"Tebrikler, bulunacak harf {bulunacakHarf} idi.")
        bayrak = True
        break

if (bayrak == False):
    print(f"Bulamadınız! Bulunacak harf {bulunacakHarf} idi.")
