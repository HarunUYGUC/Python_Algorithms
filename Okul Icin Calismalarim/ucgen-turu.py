kenar1 = float(input("Üçgenin 1. kenarını giriniz: "))
kenar2 = float(input("Üçgenin 2. kenarını giriniz: "))
kenar3 = float(input("Üçgenin 3. kenarını giriniz: "))

if (kenar1 == kenar2 == kenar3):
    print("Eşkenar üçgen!")
elif (kenar1 == kenar2) or (kenar1 == kenar3) or (kenar2 == kenar3):
    print("İkizkenar üçgen!")
else:
    print("Çeşitkenar üçgen!")


# Sözde kod (pseude-code) ile gösterilmesi:
"""
A1: Başla
A2: Yaz, "Üçgenin 1. kenarını giriniz: "
A3: Oku, kenar1
A4: Yaz, "Üçgenin 2. kenarını giriniz: "
A5: Oku, kenar2
A6: Yaz, "Üçgenin 3. kenarını giriniz: "
A7: Oku, kenar3
A8: Eğer (kenar1 == kenar2 == kenar3) ise
A8.1:   Yaz, "Eşkenar üçgen!"
A9: Eğer değilse (kenar1 == kenar2) veya (kenar1 == kenar3) veya (kenar2 == kenar3) ise
A9.1:   Yaz, "İkizkenar üçgen!"
A10: Değil ise
A10.1:  Yaz, "Çeşitkenar üçgen!"
A11: Bitir
"""
