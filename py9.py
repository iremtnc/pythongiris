# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:51:06 2024

@author: itsme
"""

#Hatalar

# print(x)     #NameError

# int("1254as")   #ValueError

# print(5/0)    # ZeroDivisionError

# print("YBS"ybs)     #SyntaxError

# print("Ybs')     # SyntaxError


try:
    print("try içindeyiz")
    # x=int("123asd")
    print(5/0)
except ValueError:
    print("Sadece sayı giriniz")
except ZeroDivisionError:
    print("0 a bölünme hatası")
except:
    print("Bir hata oluştu")
    
# kullanıcıdan 2 sayı alın. 
# print içerisinde iki sayıyı birbirine bölün
# 2. sayı sıfırsa sıfıra bölünme hatası fırlatsın
# finally blogu ekleyın


try:
    sayi1=int(input("Sayi1: "))
    sayi2=int(input("Sayi2: "))
    print(sayi1/sayi2)
    
except ZeroDivisionError:
    print("Sıfıra bölünme hatası")
    
except ValueError:
    print("Sadece sayı giriniz")
    
finally:
    print("Finally blogu her zaman çalışır")
    
    
try:
    sayi1=int(input("Sayi1: "))
    sayi2=int(input("Sayi2: "))
    print(sayi1/sayi2)
    
except (ZeroDivisionError, ValueError):
    print("ZeroDivisionError veya ValueError hatası")
    
finally:
    print("Finally blogu her zaman çalışır") 
    
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
    
x = -1

if x < 0:
  raise Exception("Üzgünüz, negatif sayılar olmaz")    
    
#raise

def stringiTerseCeviren(s):
    if(type(s) != str):
        raise ValueError ("lütfen sadece string giriniz")
    else:
        return s[::-1]
    
stringiTerseCeviren("Merhaba")
stringiTerseCeviren(12345)
    
try:
    stringiTerseCeviren(12345)
    
except: 
    print("Bir hata oluştu")
    
    
    
# Modul

import math

dir(math)
help(math)

print(pow(2,5))
print(sqrt(25)) #hatalı

print(math.sqrt(25))

print(math.ceil(11.9))  #yukarı yuvarlama
print(math.ceil(11.5))
print(math.ceil(11.1))

print(math.floor(11.9))
print(math.floor(11.5))    #aşağı yuvarlar
print(math.floor(11.1))

print(math.factorial(5))

from math import *
print(sqrt(25)) 

#Polimorfizm

class Arac():
    def __init__(self,model,marka):
        self.model=model
        self.marka=marka
        
    def hareket_et(self):
        print("Hareket Et!")
        
class Araba(Arac):
    pass

class Bot(Arac):
    def hareket_et(self):
        print("Yüz")
        
class Ucak(Arac):
    def hareket_et(self):
        print("Uç")

araba1=Araba("GLX","Mercedes")
bot1=Bot("Touring 20","ibiza")
ucak1=Ucak("747","Boeing")

for x in (araba1,bot1,ucak1):
    print(x.marka)
    print(x.model)
    x.hareket_et()
    print("")


#Polimorfizm

class Arac():
    def __init__(self,model,marka):
        self.model=model
        self.marka=marka
        
    def hareket_et(self):
        print("Hareket Et!")
        
class Araba(Arac):
    pass

class Bot(Arac):
    def hareket_et(self):
        print("Yüz")
        
class Ucak(Arac):
    def hareket_et(self):
        print("Uç")

araba1=Araba("GLX","Mercedes")
bot1=Bot("Touring 20","ibiza")
ucak1=Ucak("747","Boeing")

for x in (araba1,bot1,ucak1):
    print(x.marka)
    print(x.model)
    x.hareket_et()
    print("")

