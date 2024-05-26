# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:34:15 2024

@author: itsme
"""

listeA=[1,2,3,4] 
listeB=[1,2,3,4,5]  

listeAB=[]

for i in range(0,len(listeA)): 
    listeAB.append(listeA[i]**listeB[i]) 
    
print(listeAB) 


import numpy as np 

aa=np.array([1,2,3,4]) 
bb=np.array([5,6,7,8]) 

print(aa*bb)  

cc=np.array((1,2,3)) 
print(cc)

print(type(aa)) 

print() 


x=np.array([1,2,3]) 
print(x) 


y=np.array([(1.5,2,3),(4,5,6)]) 
print(y) 


z=np.array([[(1.5,2,3),(4,5,6)],[(1.5,2,3),(4,5,6)]])
print(z) 

t=np.array([(1.5,2,3),(4,5,6)],dtype=float)
print(t) 


t2=np.array([(1.5,2,3),(4,5,6)],dtype=int)
print(t2) 


s=np.array(99) 
print(s) 

print(s.ndim) 
print(x.ndim) 
print(y.ndim) 
print(z.ndim) 


liste=[5,6,7,8] 
l1=np.array(liste) 
print(l1) 


demet=(2,3,4,5) 
l2=np.array(demet) 
print(l2) 


l3=np.arange(10) 
print(l3) 

l4=np.arange(5,11) 
print(l4) 

l5=np.arange(0,20,2) 
print(l5) 


#Sıfır Matrisi 

l6=np.zeros(3) 
print(l6) 
print(l6.ndim) 


l7=np.zeros((3,3)) 
print(l7) 



#Birler Matrisi 

l8=np.ones(4) 
print(l8)  

l9=np.ones((4,3)) 
print(l9)


#Birim Matris 

l10=np.eye(3) 
print(l10) 

l10=np.eye((2,3)) #hatalı 


#Linspace 

l11=np.linspace(0,100,9) 
print(l11) 

l11=np.linspace(0,100,10) 
print(l11) 


l11=np.linspace(0,100,11) 
print(l11) 


#Random 

l12=np.random.randint(10)  #0-10 arası rastgele sayılar 
print(l12) 



l13=np.random.randint(5,10)  #5-10 arası rastgele sayılar 
print(l13) 


l14=np.random.randint(5,20,4)  #5-20 arası rastgele 4 sayı  
print(l14) 


l15=np.random.randint(0,100,(3,3)) 
print(l15) 

l16=np.random.rand(5) #0-1 aralığında 5 tane sayı üretir 
print(l16) 


l17=np.random.randn(5)  
print(l17) 



#Reshape -------------->kalıcı değil 

l18=np.arange(1,17) 
print(l18) 


l18.reshape(4,4) 
l18.reshape(2,8) 

l18.reshape(3,3) #hatalı 
l18.reshape(5,5) #hatalı 


#İstatiksel Bilgiler 

l19=np.random.randint(1,100,15) 
print(l19) 

l19.sum() 
l19.min() 
l19.max() 
l19.mean() 
l19.median()   #hatalı 
np.median(l19) 


"""

standart sapma: veri değerlerinin ortalamadan ne kadar uzak olduğunun ölçüsüdür.

varyans: standart sapmanın karesidir.

"""

l19.std() 
l19.var() 


#matematiksel işlemler 

a=np.array([1,2,3,4]) 
b=np.array([5,6,7,8]) 

#toplama 
print(a+b) 
print(np.add(a,b)) 

#Çıkarma 
print(a-b) 
print(np.subtract(a,b)) 

#Çarpma 
print(a*b) 
print(np.multiply(a,b)) 

#bölme 
print(a/b) 
print(np.divide(a,b)) 


#Matris çarpımı 

nd=np.array([0,1,2,3,4,5,6,7,8,9]) 

n1=nd.reshape(5,2) 
n2=nd.reshape(2,5) 

print(np.dot(n1,n2)) 


#Matrisin transpozu 

print(n1) 
print(n1.T)  

a * 2 
a**2 
a+2 
a-1 
a/2 

a.sqrt() #hatalı 

np.sqrt(a) 


#İndeksleme 

c=np.arange(0,10) 
print(c) 

c[3] 
c[1:5] 
c[2:9:2] 
c[::-1] 
c[:] 

cc=c.copy() 
print(cc) 

#Filtreleme (Mantıksal) 

cc<5  

d=np.random.randint(0,20,(3,3)) 
print(d) 

d.shape() #hatalı 
d.shape  

d.ndim
d.size  
d.dtype 

#Matris Birleştirme 

a=np.array([1,2,3,4]) 
b=np.array([5,6,7,8]) 

c=np.concatenate([a,b]) 
print(c) 

c1=np.concatenate([a,b], axis=0) #satır bazında birleştirir 
print(c1) 

c2=np.concatenate([a,b],axis=1) #hatalı 


#Matris Birleştirme (2 boyutlu) 

z1=np.random.randint(0,20(3,3)) 
z2=np.random.randint(0,20,(3,3)) 

print(z1)
print(z2) 

z3=np.concatenate([z1,z2]) #altına ekler 
print(z3) 

z4=np.concatenate([z1,z2], axis=0) #altına ekler 
print(z4)  

z5=np.concatenate([z1,z2], axis=1) #yanına ekler 
print(z5) 


#Matris Ayırma (2 boyutlu) 

x=np.arange(16).reshape(4,4) 
print(x) 

ust,alt=np.vsplit(x,2) 
print(ust) 
print(alt) 

sol,sag=np.hsplit(x,2) 
print(sol)
print(sag) 

x1,x2,x3,x4=np.hsplit(x,4) 
print(x1)





l20=np.random.randint(1,100,50) 
print(l20) 

l20.sum() 
l20.min() 
l20.max() 
l20.mean() 
np.median(l20) 
l20.std()
l20.var() 
np.sort(l20) 

import numpy as np
# Öğrenci numaraları
student_ids = np.arange(1, 11)

# Öğrenci isimleri
student_names = np.array(['Ali', 'Ayşe', 'Ahmet', 
                          'Fatma', 'Mehmet', 'Elif', 
                          'Can', 'Deniz', 'Ece', 'Emre'])

# Ders isimleri
subjects = np.array(['Matematik', 'Fizik', 'Kimya', 'Biyoloji', 'Tarih'])

# Rastgele notlar (0-100 arasında)
grades = np.random.randint(0, 101, size=(len(student_ids), len(subjects)))

# Öğrenci numaraları, isimleri ve notları birleştirerek bir veri seti oluşturma
student_data = np.column_stack((student_ids, student_names, grades))

# Veri setini yazdırma
print("Öğrenci Veri Seti:")
print("Öğrenci No, İsim, Matematik, Fizik, Kimya, Biyoloji, Tarih")
for row in student_data:
    print(row) 
    
    









