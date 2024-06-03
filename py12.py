# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:39:18 2024

@author: itsme
"""

#Matplotlib 

import matplotlib.pyplot as plt 
import numpy as np 

x=np.array([0,5])  #☺ 1. nokta ( 0,10) ve 2. nokta( 5,50)
y=np.array([10,50])  

plt.plot(x,y)  
plt.plot(x,y,'o')   

x1=np.array([1,2,5,9]) 
y1=np.array([3,5,1,11]) 

plt.plot(x1,y1) #doğru olarak çizer 

a=np.array([2,5,6,9,1])  #y ekseni olarak algılar, xler 0,1,2 olarak devam eder 

plt.plot(a) 

#MARKER ÇEŞİTLERİ 

plt.plot(a,marker='o') #doğruyu ve noktaları gösterir 
plt.plot(a,'o') #sadece noktaları gösterir

plt.plot(a,marker='x') 
plt.plot(a,marker='X') #kalın x 
plt.plot(a,marker='+', ms=20)   #ms=marker size 
plt.plot(a,marker='P', ms=20) #P = plus (kalın artı)
plt.plot(a,marker='.', ms=20) #daha küçük nokta 
plt.plot(a,marker='d', ms=20) 
plt.plot(a,marker='D', ms=20) 
plt.plot(a,marker='h', ms=20) 
plt.plot(a,marker='H', ms=20) 
plt.plot(a,marker='<', ms=20) 
plt.plot(a,marker='>', ms=20) 
plt.plot(a,marker='|', ms=20)  
plt.plot(a,marker='_', ms=20)  
plt.plot(a,marker='*', ms=20) 



#ÇİZGİ ÇEŞİTLERİ

plt.plot(a,'-') 
plt.plot(a,'--')
plt.plot(a,':') 
plt.plot(a,'-.') 

plt.plot(a, linestyle='dotted',linewidth=10)    #plt.plot(a, ':')   
plt.plot(a, linestyle='dashed',linewidth=10) 

plt.plot(a, ls='-.', linewidth=10)  

plt.plot(a, color='red', linewidth=5) 
plt.plot(a, color='cyan', linewidth=5)  

plt.plot(a, color='yellow', linewidth=5)   

plt.plot(a, '--P', color='green') 
plt.plot(a, '*--', color='orange')    


#RENKLER 

plt.plot(a, 'o--y')  
plt.plot(a, 'D--m')  
plt.plot(a, '*:g') 

#ms: marker size 
plt.plot(a, '*:g',ms=20) 

#marker edge color(mec) 
plt.plot(a, '*:g',mec='y', ms=20)  

#marker face color (mfc) 
plt.plot(a, '*:g',mec='r',ms=20,mfc='b') 

#hecadecimal color 

#çoklu çizgiler 

y1=np.array([1,2,5,8]) 
y2=np.array([3,5,1,9])

plt.plot(y1) 
plt.plot(y2) 


x1=np.array([1,2,5,7]) 
y1=np.array([0,2,5,4]) 

x2=np.array([1,3,5,7]) 
y2=np.array([0,2,7,4])


plt.plot(x1,y1,x2,y2) 

#eksen etkileri 

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

#başlık ekleme 

plt.title("Başlık") 

plt.grid()  #ızgara görünümü 
plt.grid(axis='x') 
plt.grid(axis='y') 
plt.grid(color='g', linestyle=':', linewidth=5) 

plt.grid(color='b', linestyle='--', linewidth=1) 


#yan yana grafikler 

x1=np.array([1,2,5,7]) 
y1=np.array([0,2,5,4]) 
plt.subplot(2,1,1) #(satır,sütun,hücre) 
plt.plot(x1,y1) 



x2=np.array([1,3,5,7]) 
y2=np.array([0,2,7,4]) 
plt.subplot(2,1,2)
plt.plot(x2,y2) 


#4 grafik 

x1=np.array([1,2,5,7]) 
y1=np.array([0,2,5,4]) 
plt.subplot(2,2,1) #(satır,sütun,hücre) 
plt.plot(x1,y1) 



x2=np.array([1,3,5,7]) 
y2=np.array([0,2,7,4]) 
plt.subplot(2,2,2)
plt.plot(x2,y2) 

x3=np.array([1,2,5,7]) 
y3=np.array([0,2,5,4]) 
plt.subplot(2,2,3) #(satır,sütun,hücre) 
plt.plot(x3,y3) 



x4=np.array([1,3,5,7]) 
y4=np.array([0,2,7,4]) 
plt.subplot(2,2,4)
plt.plot(x4,y4) 


#Diğer grafikler 

plt.scatter(x1,y1) 
plt.scatter(x2,y2) 

plt.scatter(x1,y1,x2,y2) 

plt.bar(x1,y1) 

x1=np.array([1,2,5,7]) 
y1=np.array([0,2,5,4]) 
plt.bar(x1,y1) 

plt.barh(x1,y1) #yatay sütun 

x=np.random.normal(10,20,200) 
plt.hist(x) 


y1=np.array([2,5,20,3]) 
plt.pie(y1) 

































