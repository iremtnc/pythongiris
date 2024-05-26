# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:35:14 2024

@author: itsme
"""

liste=[1,2,3,4,5,6,7,8,9,10] 
print(liste[::2]) #tek 
print(liste[::-1]) #kalıcı değil 

dir(list) 

liste1=[1,2,3,4]
liste2=[5,6,7,8] 

liste3=liste1+liste2 
print(liste3)

liste1.extend(liste2)  #ekleme yapar 
print(liste1) 

liste1=liste1+[9] 
print(liste1) 

liste1=liste1 + ["a"] 
print(liste1) 

print(liste2 * 2)  

#append 

liste1=[0,1,2,3]
liste1.append(4) 
print(liste1) 

bosListe=[]
bosListe.append(100) 
print(bosListe) 

#reverse 

liste1.reverse() #kalıcı olarak değişir 
print(liste1) 

#pop 

liste1.pop() #default olarak en sondaki elemanı siler 
liste1.pop(0) #indeksi 0 olanı kaldırır 
liste1.pop(1) 

#sort 

liste1=[2,3,35,6,8,9,-2,-3,-8,25] 
liste1.sort() 
print(liste1)  #kalıcı bir işlem, default olarak küçükten büyüğe yazdırır 

liste1.sort(reverse=True) #büyükten küçüğe yazdırır 

#iç içe listeler 

L1=[1,2,3]
L2=[4,5,6] 
L3=[7,8.9] 

listeb=[L1,L2,L3] 
print(listeb) 
print(len(listeb)) 

print(listeb[1][1]) 
print(listeb[2][2]) 


#demetler(tuple) 

demet=(1,2,3,4)
print(type(demet)) 

#listelere benzerler fakat değiştirilemezlerdir 

print(demet[0]) 
print(demet[3])
print(demet[10]) #hatalı 

dir(tuple) 

demet=(1,5,6,89,-5,"merhaba","z",5.6)  
print(demet.index("merhaba")) 
print(demet.index(1)) 
print(demet.index(10)) #value error 

demet2=(1,1,1,2,2,3,3,3,4,4,4,4,5,6,6,6) 
print(demet2.count(1)) 
print(demet2.count(3)) 
print(demet2.count(10)) 

demet2[0]=10 #değiştirilemez 

#sözlükler / dict 

sozluk={"book" : "kitap","apple":"elma","orange":"portakal"}   
print(type(sozluk))  

dir(dict)  

print(sozluk.keys()) 
print(sozluk.values())  

print(sozluk(0)) #hatalı 

print(sozluk["book"]) #keys de çalışır 
print(sozluk["kitap"]) #hatalı 

#dict={keys:values} 

#iç içe sözlükler 

sozluk2={"aylar:":{"ocak":1,"şubat":2,"mart":3},
         "sayılar" :{"bir":1,"iki":2,"üç":3}}  

print(sozluk2)

print(sozluk2["aylar:"])  
print(sozluk2["sayılar"])

print(sozluk2["aylar:"]["şubat"]) 


#INPUT

sayi1=input() #string olarak okur 

print(type(sayi1)) 

sayi1=input("Lütfen bir sayı giriniz:") 
sayi1=int(input("sayı giriniz:")) 

sayi2=int(input("sayı giriniz:")) 

print("Toplam=",sayi1+sayi2) 

a=input("sayı giriniz:") 
print(a*3) #üç defa yazar 

a=int(input("sayı giriniz:"))
print(a*3) 

b=float(input("sayı giriniz:")) 
print(b) 


sayia=int(input("1.sayıyı girin:"))  
sayib=int(input("2.sayıyı sayı girin:")) 
sayic=int(input("3.sayıyı girin:")) 
  

print("Toplam=", sayia+sayib+sayic) 

#koşullu ifadeler 

#if
#if, else  
#if, elif,elif,....,else 

#Hesap Makinesi 

print("""
      İşlemler
      1.Toplama
      2.Çıkarma
      3.Çarpma
      4.Bölme
      """) 
      
islem=int(input("Lütfen işlem numarasını giriniz:")) 

sayi1=float(input("1. sayı:")) 
sayi2=float(input("2.Sayı:")) 

if(islem==1):
    print("{}+{}={}".format(sayi1,sayi2,sayi1+sayi2)) 

elif(islem==2): 
    print("{}-{}={}".format(sayi1,sayi2,sayi1-sayi2)) 
    
elif(islem==3): 
        print("{}*{}={}".format(sayi1,sayi2,sayi1*sayi2)) 

elif(islem==4): 
    print("{}/{}={}".format(sayi1,sayi2,sayi1/sayi2))  
    
else:
    print("Geçersiz işlem numarası")  








