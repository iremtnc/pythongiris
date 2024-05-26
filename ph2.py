# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:53:05 2024

@author: itsme
"""

isim="İrem" 
isim[0] 
isim[3] 

isim[-1] 
isim[-10] #ındex error 

isim[-0] 

a="python programlama" 
a[0:5] #0. ındexten itibaren 5 karakter verir
a[2:10] 
a[:] #hepsini yazdırır 
a[:12]  #12. karaktere kadar gider 
a[2:] #2. karakterden itibaren hepsini yazdırır 
a[:-5] #son 5 karakteri yazdırmaz  
a[-10:-2] 

a[1:10:2] #ilk karakterden itibaren 2şer atlayarak 10. karaktere kadar yazdırır 
a[::2] #başan itibaren 2şer atlayarak yazdırır 
a[::3] 
a[::-1] #tersten yazdırır 

isim[::-1] 

len(isim) 

x="Merhaba"
y="Dünya" 

x+y 
x*3 

#hatalı 
x-3
x+3
x/3 

#yorum satırı 
"""

yorum
satırı

""" 

""" 
değişken isimleri 
* sayı ile başlaması
* kelimeler arası boşluk olmasın
* :''"".<>?!()@#_?=)(/&%+^'!')  sembol kullanamazsın kısacası alt tire hariç 
* kodlamaya özel kelimeleri kullanamazsın (true, no, do) 
"""

sayi1=20
sayi2=25 
sayi3=sayi1+sayi2 

#hatalı 
#1sayi=20  #sytnax error 
#bir sayi=20  
#while=15 

birSayi=20 
bir_sayi=20 

9+5 
9-8
98//5 
98%5 

sayi1=20
sayi2=25 

#b1. yol 
gecici=sayi1 
sayi1=sayi2 
sayi2=gecici 

#2.yol 
sayi1=sayi2, sayi2=sayi1 #sonra bak 

a=20
a = a+1 
a+=1 
#a++ #hatalı 


#stringler 
print("Merhaba")  
print("Merhaba", "Dünya ")  
print("Merhaba",12,15,18)   
print("Merhaba", 12,15,18,25.25,52.78)   

print("Merhaba \nDünya")  
print("Merhaba \tDünya") #bir tab boşluk bırakır 

print(""" 
      
      Merhaba
      Arkadaşlar
      Nasılsınız""")  

#TYPE FONKSİYONU 

a=55 
print(type(a)) 
b=5.89 
print(type(b)) 
c="Merhaba" 
print(type(c)) 
d='a' 
print(type(d))  


#sep parametresi 

print(1,2,3,4,5, sep=".") 
print(7,3,2024, sep=",") 

print("ocak", "şubat", "mart", sep="/")    
print("ocak", "şubat", "mart", sep="\n") 
print("ocak", "şubat", "mart", sep="\t")  

print(*"irem") 
print(*"İrem", sep="\n") 
print(*"TBMM" , sep=".") 


#formatlama 

x=5
y=10 

print("{} + {} = {}".format(x,y,x+y))  
print("{}  {}  {}".format(7,3,2024))  

print("{1}  {0}  {2}".format(7,3,2024)) #sırayı değiştirir 

print("{} {} {}".format(3.54546,4.545456,5.12156)) 
print("{:.3f} {:.2f} {:.1f}".format(3.54546,4.545456,5.12156)) 


#Listeler

liste=[1,2,3,4,5]  
print(liste) 
print(type(liste)) 

liste2=["a","b","c"] 
print(liste2) 

liste3=["merhaba" , "dünya"] 
print(liste3) 

liste4=[1,2,3,"merhaba", 5.5] 
print(liste4) 

#boş liste 

bos_liste=[] 
bos_liste2=list() 

#listenin boyutu 
print(len(liste)) 
print(len(liste2)) 

s="İrem" 
liste5=list(s) 
print(liste5) 

print(liste) 
liste[0] 
liste[4] 
liste[10] #ındex error 

liste[-1] 
liste[-2] 
liste[-10] #ındex error 

#listenin son elemanı 

print(liste[-1]) 
print(liste[len(liste)-1]) 
print(liste[0]) #listenin ilk elemanı 

print(liste[:3]) 
print(liste[1:]) 

liste6=[1,2,3,4,5,6] 
print(liste6[::2]) #tek 
print(liste6[::-2]) #kalıcı değil 

