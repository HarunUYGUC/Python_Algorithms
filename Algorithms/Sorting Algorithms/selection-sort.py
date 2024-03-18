liste = [7, 4, 10, 8, 3, 1]
print(f"Listenin karışık hali: {liste}")

for i in range(0, len(liste) - 1):
    enKucuk = liste[i]
    enKucukIndis = i
    for j in range(i + 1, len(liste)):
        if (liste[j] < enKucuk):
            enKucuk = liste[j]
            enKucukIndis = j

    tutucu = liste[i]
    liste[i] = liste[enKucukIndis]
    liste[enKucukIndis] = tutucu

print(f"Listenin küçükten büyüğe sıralanmış hali: {liste}")
