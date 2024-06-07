# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:53:38 2024

@author: itsme
"""

import seaborn as sns 
df = sns.load_dataset("planets") 

df.info() 

#Veri Temizleme 

yeni_df = df.dropna() 
yeni_df.info() 


#Boş verilerin doldurulması 

yeni_df2 = df.fillna(0) 
yeni_df2.info() 


#Orbital_period ortalaması 

op_ort = df["orbital_period"].mean() 
print(op_ort) 

yeni_df3 = df 

yeni_df3.describe() 

yeni_df4=yeni_df3["orbital_period"].fillna(op_ort) 
yeni_df4.describe() 

#Aynı verileri silme 

yeni_df5=df.duplicated()  

yeni_df5=df.drop_duplicates() #♣tekrar eden verileri siler 
yeni_df5.describe() 


import numpy as np 
from scipy import stats 

s = [23,25,36,89,4,1,5,25,6,78,11] 

ortalama=np.mean(s) 
print(ortalama) 

medyan = np.median(s) 
print(medyan)

dir(stats) 

mod_S=stats.mode(s) 
print(mod_S) 

standartSapma=np.std(s) 
print(standartSapma)

s2=[67,66,68,70,69,65,66,68,59,70]
standartSapma2=np.std(s2) 
print(standartSapma2)


#Yüzdelikler 

yas = [23,25,28,29,35,42,35,32,23,26,50]

ceyrek75=np.percentile(yas,75) 
print(ceyrek75)

#yüzde 75i 35in altındadır 

ceyrek90=np.percentile(yas,90) 
print(ceyrek90)















