liste = [7, 4, 10, 8, 3, 1]
print(f"Listenin karışık hali: {liste}")

for i in range(0, len(liste) - 1):  # Listenin tamamının sırlanması için kurulan döngü.
    for j in range(0, len(liste) - 1 - i):  # İkili karşılaştırma ve sıralama için kurulan döngü.
        if (liste[j] > liste[j + 1]):
            buyukEleman = liste[j]
            liste[j] = liste[j + 1]
            liste[j + 1] = buyukEleman

print(f"Listenin küçükten büyüğe sıralanmış hali: {liste}")


# "Sözde Kod (pseude-code)" ile gösterilmesi:
"""
liste = [7, 4, 10, 8, 3, 1]
FOR (i; 0 to (liste eleman sayısı - 1), STEP = 1)
    FOR (j; 0 to (liste eleman sayısı - 1 - i), STEP = 1)
        IF (liste[j] > liste[j + 1]) THEN
            buyukEleman = liste[j]
            liste[j] = liste[j + 1]
            liste[j + 1] = buyukEleman
        ENDIF
    ENDFOR
ENDFOR
WRITE "Listenin küçükten büyüğe sıralanmış hali: " + liste
"""
