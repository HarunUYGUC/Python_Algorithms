liste = [7, 4, 10, 8, 3, 1]
print(f"Listenin karışık hali: {liste}")

for i in range(1, len(liste)):
    for j in range((i - 1) , -1, -1):
        if (liste[j + 1] < liste[j]):
            tutucu = liste[j + 1]
            liste[j + 1] = liste[j]
            liste[j] = tutucu
        else:
            break

print(f"Listenin küçükten büyüğe sıralanmış hali: {liste}")
