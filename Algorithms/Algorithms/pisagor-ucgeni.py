def pisagor():
    pisagor_ucgeni = list()

    for i in range(1, 101):
        for j in range(1, 101):
      
            x = (i**2 + j**2)**(0.5)
      
            if (x == int(x)):
                pisagor_ucgeni.append((i, j, int(x)))
        
    return pisagor_ucgeni


for i in pisagor():
    print(i)
