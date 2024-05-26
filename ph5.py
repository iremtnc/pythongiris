# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:57:54 2024

@author: itsme

""" 

#WHILE 

""" 
while (koşul): 
    alt kod 
"""

i=0 

while(i<10): 
    print(i) 
    i+=1 

#0-20 arası 3ün katlarını yazdırma 

i=0

while(i<20):
    print(i) 
    i += 3 
    
liste=[1,5,6,8,45,11] 
i=0 
while(i<len(liste)): 
    print("İndeksi:" , i, "Değeri:", liste[i]) 
    i+=1 
    
    
    
    
 #break ve continue 

i=0 
while(i<15): 
    print(i) 
    if(i==10):   #10 u yazar ve döngüden çıkar 
        break 
    i +=1 
    
    
    
i=0 
while(i<15): 
        print(i) 
        if(i==10):   #sonsuz döngüye girer 
            continue
        i +=1
    
    
for i in range (0,20): 
    if (i==10):        #10a kadar yazar ve döngüden çıkar 
        break 
    print(i) 
   
#10u yazmasını istersek önce print yazılmalı 


while True: 
    isim=input("İsminizi yazınız(Çıkış için c):")
    if(isim=="c" or isim=="C"): 
        print("Çıkış yapılıyor...") 
        break 
    print(isim) 
    
    
    
while True: 
    sayi=int(input("Bir sayı giriniz(Çıkış için -1):"))
    if(sayi == -1): 
        print("Çıkış yapılıyor...") 
        break 
    print(sayi) 
    

# faktöriyel 

while True:
    sayi=int(input("Sayı(Çıkış: -1)")) 
    if (sayi== -1 or sayi<0): 
        print("Çıkış yapılıyor...") 
        break 
    faktoriyel=1 
    for i in range(2,sayi+1) :
        faktoriyel *=i 
        print("Faktöriyeli:", faktoriyel) 


def faktoriyel(sayi): 
    faktoriyel = 1 
    for i in range(2,sayi+1): 
        faktoriyel *=i 
        print(faktoriyel) 
        
faktoriyel(5) 


#METOTLAR 

def selamlama(): 
    print("Merhaba") 
    
selamlama() 
    
type(selamlama) #function 
type(selamlama()) #nonetype 

def selamlama2(isim): 
    print("Merhaba", isim) 
    
selamlama2("İrem") 

def toplama(a,b,c): 
    print("Toplamı:" , a+b+c) 
    
toplama(10,20,30) 
toplama(2,5,9) 
toplama(-10,5,6) 

toplama(10,20) #hatalı 
toplama(10,20,30,40) #hatalı 

def toplama2 (a,b,c): 
    return a+b+c 

print("Toplam:", toplama2(10,5,-8)) 

def ucKati(a): 
    return a*3 

print("Sayının üç katı:", ucKati(4)) 

def selamlama3(isim="isimsiz"): 
    print("Merhaba", isim) 
    
selamlama3() 
selamlama3("İrem")    

def bilgileriGetir(ad="Bilgi yok", soyad="Bilgi yok", no="Bilgi yok"):
    print(ad,soyad,no) 
    
bilgileriGetir("İrem", "Tunç", 105)
bilgileriGetir("İrem", 105) 
bilgileriGetir("Tunç", 105) #veri kayması  
bilgileriGetir(ad="Zeynep", no=105) 


#parametreler 

def toplama3(*parametreler): 
    print("Parametreler:", parametreler) 
    toplam=0 
    for i in parametreler:
        toplam+=i 
    return toplam 

print("Toplam:", toplama3(2,3,5,6,-10,89))


# Yerel ve Global Değişkenler 

a=10 

def fonksiyon(): 
    a=20 
    print("Fonksiyonun içindeki değer:", a) 
    
fonksiyon() 
print("Fonksiyonun dışındaki değer:", a) 



a=10 

def fonksiyon(): 
     global a
     a=20 
     print("Fonksiyonun içindeki değer:", a) 
        
fonksiyon() 
print("Fonksiyonun dışındaki değer:", a) #20 
    
    

# List Comprehension 
    
liste1=[1,2,3,4,5] 
liste2=[]     

for i in liste1: 
    liste2.append(i) 


liste3=[i for i in liste1]       

liste4=[i*3 for i in liste1]    
    
liste5=[(1,2),(3,4),(5,6)] 

liste6=[i*j for i,j in liste5] 

m="YBS"

liste7=[i for i in m] 

liste8=[i*4 for i in m] 
    

#Lambda -------------> metodları kısaca yazabilirsin 

def ikiKa(sayi):
    return sayi*2 

ikiKa(40) 

ucKati2=lambda x : x*3 
ucKati2(15) 


toplama4 = lambda x,y,z : x+y+z 
toplama4(10,25,-8)  


# Asal mı? 

def asalMi(sayi): 
    if(sayi==1): 
        return False 
    elif(sayi==2): 
        return True 
    else: 
        for i in range (2,sayi): 
            if(sayi % i==0):
                return False 
        return True 
    
asalMi(10) 
asalMi(5) 


#Tam bölenleri

def tambolenleri(sayi):
    tambolenler=[] 
    for i in range (2,sayi+1): 
        if(sayi % i==0): 
            tambolenler.append(i) 
    return tambolenler 

tambolenleri(20) 
tambolenleri(1107) 
tambolenleri(997) 

















    
    