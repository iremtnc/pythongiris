# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:12:44 2024

@author: itsme
"""

#NOT DÖNÜŞÜMÜ

ortPuan=int(input("Notunuzu giriniz:")) 

if(ortPuan>=90):
    print("AA") 
elif(ortPuan>=80): 
    print("BB") 
elif(ortPuan>=70):
    print("CC") 
elif(ortPuan>=60): 
    print("DD") 
else:
    print("FF") 
    

#MANTIKSAL BAĞLAÇLAR: AND, OR, NOT 

print(1>5) 
print(5>2) 

#AND

print(True and False) 
print(False and True) 
print(True and False) 
print(False and False) 

print(1<5 and "YBS"=="ybs") 
print(1<5 and "YBS"=="YBS")
print(1<5 and "YBS"!="ybs")  

#OR 

print(True or True) 
print(False or True)
print(True or False) 
print(False or False) 

print(3.4 >2.5) 
print(3.2<5.8 or "ybs" != "ubf") 

#NOT

print(1) 
print(not 1) 
print(not 10) 

print(0) 
print(not 0)
print(not -8) 
print(not 2.5) 

print(not "python"=="PYTHON" and 1==0 or (4.5 < 1.6 or 5!=5)) 

print(True and False or(False or True)) 
print(True and False or False) 
print(False or False) 

print(not True or False) #sadece kendi sağındakini etkiler 

print("a" < "A") #false 
print("a" < "z") #true 

#BOOL 

bool(5<9) 
bool(8<5) 

bool(0) 
bool(1) 
bool(45)
bool(-5)
bool(5.7) 

bool("a" > "c") 

bool("Merhaba") 


#KULLANICI GİRİŞİ 

print("Kullanıcı girişi") 

kullaniciAdi="İrem" 
sifre="12345" 

girilenKullaniciadi=input("Kullanıcı Adı:") 
girilenSifre=input("Şifre:") 

if(kullaniciAdi!=girilenKullaniciadi and sifre==girilenSifre): 
    print("Kullanıcı adı hatalı") 
elif(kullaniciAdi==girilenKullaniciadi and sifre!=girilenSifre): 
    print("Şifre hatalı") 
elif(kullaniciAdi != girilenKullaniciadi and sifre!= girilenSifre):
    print("Kullanıcı adı ve şifre hatalı") 
else: 
    print("Hoş geldiniz", kullaniciAdi) 

    
#in 

print("a" in "merhaba") 
print("z" in "merhaba") 
print("aba"in "merhaba") 


print(4 in [1,2,3,4]) 
print(7 in [1,2,3,4,5,6]) 

print(4 in [1,2,4,5,6]) 

#for 

liste=[1,2,3,4,5] 

for i in liste: 
    print(i) 
    
for i in liste: 
    print(i**3) 
    
    
toplam=0 

for i in liste:
   toplam+=i 
   print("Toplam:" , toplam) 
   
liste2=[2,5,7,21,14,8,9,-8] 

for i in liste2:
    if(i % 7 ==0): 
        print(i) 
  
s="YBS" 

for i in s: 
    print(i*3) 

demet = (1,2,3,4,5) 

for i in demet: 
    print(i*5) 

sozluk= {"bir":1, "iki":2, "üc":3} 

for i in sozluk: 
    print(i) #sadece keyler yazılır 
    
for i in sozluk.values(): 
    print(i) 
    
for i in sozluk.keys(): 
    print(i) 
    

sayi=int(input("Lütfen bir sayı giriniz:")) 

if(sayi % 2==0): 
    print("Girilen sayı çifttir")
else: 
    print("Girilen sayı tektir") 
        

#range 

print(range(10)) 
print(*range(10)) #bitiş değeri dahil değil 

print(*range(5,10)) 

print(*range(10,100,10)) 

print(*range(105,111)) 

print(*range(100,0,-10)) 


liste=list(range(1,21)) 
print(liste) 

for i in range(1,11): 
    print("*") 

for i in range(1,11): 
    print("*" * i)  
    

#Fibonacci Seri 

#a,b=b,a    iki sayının yerini değiştirme 

birinciSayi=1 
ikinciSayi= 1 

fibonacci = [birinciSayi, ikinciSayi] 

sayac = int(input("Kaç terim yazılsın:")) 

for i in range(sayac-2): 
    birinciSayi, ikinciSayi = ikinciSayi, birinciSayi+ikinciSayi 
    fibonacci.append(ikinciSayi) 
    
print(fibonacci) 









