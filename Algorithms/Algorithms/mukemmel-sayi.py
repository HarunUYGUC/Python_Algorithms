print("--- 1000'den Küçük Mükemmel Sayılar ---")

for num in range(1, 1001):
    sum = 0

    for divisor in range(1, (num//2 + 1)):
        if (num % divisor == 0):
            sum += divisor
    
    if (num == sum):
        print(num)
