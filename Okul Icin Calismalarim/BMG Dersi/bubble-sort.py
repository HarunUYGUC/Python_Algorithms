liste = [45, 15, 23, 17, 88, 35, 75, 28, 13, 98, 1, 56, 14, 14, 73]
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
liste = [45, 15, 23, 17, 88, 35, 75, 28, 13, 98, 1, 56, 14, 14, 73]
FOR (i; 0 to (liste eleman sayısı - 1)) THEN
    FOR (j; 0 to (liste eleman sayısı - 1 - i))
        IF (liste[j] > liste[j + 1]) THEN
            buyukEleman = liste[j]
            liste[j] = liste[j + 1]
            liste[j + 1] = buyukEleman
        ENDIF
    ENDFOR
ENDFOR
WRITE "Listenin küçükten büyüğe sıralanmış hali: " + liste
"""
