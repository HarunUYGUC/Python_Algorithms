# Basit yoldan asal sayı bulma yöntemi.
# https://jn7.net/girilen-iki-sayinin-asal-bolenlerini-ekok-bulma/

def asal(a):
    if a == 1 :
        return False
    elif a == 2 or a==3 or a==5 or a==7: #Daha az işlemle asal sayıyı bulmak için belli sayıları True döndürüyoruz
        return True
    elif a%2== 0 or a%3==0 or a%5==0 or a%7==0: #İşlemleri hafifletmek için tüm çift sayıları, 3,5 ve 7 nin katlarını False döndürüyoruz
        return False
    else:
        for i in range(3,a): #3 ten başlayarak sayının kendisine kadar olan tüm sayılara bölünüp bölünmediğini kontrol ediyoruz.
            if a%i==0:
                return False
    return True


# Gelişmiş yönden asal sayı bulma yöntemi.
# https://jn7.net/python-ornekleri-asal-sayi-bulucu/

def asalSayiBul(n): #n sayisina kadar olan asal sayıları bulur
    k=0
    asalSayilar = [True for i in range(n+1)] # istenilen n sayısı büyüklüğünde her elemanı true olan bir dizi oluşturuyoruz
    # örnek n = 10  için [True,True,True,True,True,True,True,True,True,True] gibi
    
    p=2 #en küçük asal sayı 2 den başlıyoruz
    while(p*p <=n): # p sayısının karesi n den küçük  olduğu sürece devam edecek
        
        if(asalSayilar[p]==True): # Eğer sayının karşılığı dizi içinde true ise asal olup olmadığını kontrol ediyoruz
            
            for i in range(p*2,n+1,p): 
                asalSayilar[i]= False #eğer sayı asal değilse sayıyı ve sayının katlarını dizi içindeki yerlerini false yapıyoruz bu sayede tekrar aynı sayıları kontrol etmeyeceğiz
                
        p+=1
        
    for p in range(2,n):
        if asalSayilar[p]:
            k+=1
            if (k==10001):
                print(k,". ci asal sayi : ", p)
               
asalSayiBul(1000000)


# Daha da gelişmiş yönden asal sayı bulma yöntemi.
# https://jn7.net/python-ornekleri-asal-sayi-bulucu/

def asalSayiBul(n): #n sayisina kadar olan asal sayıları bulur
    k=0
    topla = 0
    asalSayilar = [True for i in range(n+1)] # istenilen n sayısı büyüklüğünde her elemanı true olan bir dizi oluşturuyoruz
    # örnek n = 10  için [True,True,True,True,True,True,True,True,True,True] gibi
    
    p=2 #en küçük asal sayı 2 den başlıyoruz
    while(p*p <=n): # p sayısının karesi n den küçük  olduğu sürece devam edecek
                                                                                                                                                                                  
        if(asalSayilar[p]==True): # Eğer sayının karşılığı dizi içinde true ise asal olup olmadığını kontrol ediyoruz
            
            for i in range(p*2,n+1,p): 
                asalSayilar[i]= False #eğer sayı asal değilse sayısı ve sayının katlarını dizi içindeki yerlerini false yapıyoruz bu sayede tekrar aynı sayıları kontrol etmeyeceğiz
                
        p+=1
        
    for p in range(2,n):
        if asalSayilar[p]:
            k+=1
            topla = topla + p
    return topla
                        
print("toplam : " , asalSayiBul(2000000))
