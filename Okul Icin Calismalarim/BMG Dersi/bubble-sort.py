liste = [15, 45, 23, 17, 88, 35, 75, 28, 13, 98]
print(f"Listenin karışık hali: {liste}")

for i in range(0, len(liste)):  # Listenin tamamının sırlanması için kurulan döngü.
    for j in range(0, len(liste) - 1):  # İkili karşılaştırma ve sıralama için kurulan döngü.
        if (liste[j] > liste[j + 1]):
            buyukEleman = liste[j]
            liste[j] = liste[j + 1]
            liste[j + 1] = buyukEleman

print(f"Listenin küçükten büyüğe sıralanmış hali: {liste}")
