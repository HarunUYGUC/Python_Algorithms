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


"""Bu uygulamanın "Sözde Kod"undaki "rastgele harf seçme" önemli. Dikkat et!!!"""
# "Sözde Kod (pseude-code)" ile gösterilmesi:

"""
x = random(26) + 65
bulunacakHarf = ASCIIKar(x)     # ASCII tablosunda büyük harfler 65 - 90 arasında denk geldiği  
WRITE "Kaç hakta büyük harfi bulmak istersiniz?: " # için böyle bir kod yazılması gereklidir.
GET kacHak
i = 0
flag = False
LOOP (i < kacHak) THEN
    WRITE "Tahmininizi giriniz: "
    GET tahmin
    i = i + 1
    IF (tahmin == bulunacakHarf) THEN
        WRITE "Tebrikler, bulunacak harf " + bulunacakHarf + " idi."
        flag = True
        break
    ENDIF
ENDLOOP
IF (flag == False) THEN
    WRITE "Bulamadınız! Bulunacak harf " + bulunacakHarf + " idi."
ENDIF
"""
