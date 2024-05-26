# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:38:20 2024

@author: itsme
"""

print("Hello World")  

x="Merhaba"
y="Dünya"
x+y

a=10
b=5.2

c=float(a)
d=int(b)

print(c) 
print(d)

print(float(15))
print(int(10.5))
print(int(10.9))
print(int(10.1))

e=4578
f=str(e)
print(f)

len(e) #hatalı
len(12547)
len(f) #sadece stringlerde çalışır

g=45.45
i=str(g)
print(i)
len(i)

a="12345"
b=int(a)
print(b)

c="asdasfs" #ValueError
d=int(c)
print(d)

e="45.45asd" #ValueError
f=float(e)

#Matematiksel Operatorler

x=23
y=6
z=12

print(x + y)
print(x + y + z)
print(x - y)
print(x * y)
print(z / y)  #her zaman float olur 

#Tam Bolme
print(x / y)
print(x // y)  # bölüm ü verir 

#mod alma 
print(x % y) 

#kuvvet alma
print(z ** y)
print(2 ** 3)
print(5 ** 2)

#karekok
print(25 ** 0.5)

print(10 ** 3) 
print(10 ** -3)

z=45
print(-z)

#işlem önceliği
     #parantez içi
     #kuvvet alma / mod alma
     #çarpma / bölme / tam bolme
     #toplama / çıkarma
     #sol -> sağ
print(9 + 5 // 2 - 1 * 3)   
print(5**4/2)
print(8/4**3)  
print(11 % 3 * 2) 

#Stringler

print("Merhaba")
print('Merhaba')
print("""Merhaba""")

print("""   Merhaba 
      Dünya""")

print("Bandırma'da hava çok sisli")
#print('Bandırma'da hava çok sisli') #hatalı
      
isim="Zeynep" 

isim[0]
isim[5]
isim[10]  #hatalı

isim[-1] 
isim[-6]    



