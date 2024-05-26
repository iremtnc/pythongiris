# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:45:03 2024

@author: itsme
"""

import pandas as pd 

a=pd.Series([1,2,3,4,5])
print(a) 

print(a.sum()) 
print(a.min())
print(a.max()) 
print(a.mean()) 
print(a.median())

data={'isim':['Ahmet','Elif','Mehmet','Zeynep'],
      'Yaş':[28,22,35,42],
      'Şehir':['istanbul','Ankara','İzmir','Bursa']} 

print(data)

df=pd.DataFrame(data) 
print(df)



#Veri okuma

df_csv=pd.read_csv('dosya_yolu.csv') 
df_excel=pd.read_excel('dosya_yolu.csv') 


#Veri inceleme 

print(df.head()) #ilk 5 satırı gösterir 

print(df.info()) 

print(df.describe()) #numerik bilgileri verir 


#Veri Seçimi 

yaslar=df['Yaş'] 
print(yaslar) 


gencler=df[df['Yaş']<30]   
print(gencler) 

#Yeni sütun ekleme 

df['Yaş kategorisi'] =['genc' if yas<30 
                       else 'yetiskin' for yas in df['Yaş']] 


print(df) 

df['Şehir']=df['Şehir'].str.upper() 
print(df) 

sehir_yas_ort=df.groupby('Şehir')['Yaş'].mean 
print(sehir_yas_ort) 



#Tarih / Zaman 

df['dogum tarihi'] =pd.to_datetime(['1992-01-16',
                                    '2000-05-25',
                                    '1985-09-30',
                                    '1978-07-22']) 


df['yil']=df['dogum tarihi'].dt.year 
df['ay']=df['dogum tarihi'].dt.month 
df['gun']=df['dogum tarihi'].dt.day 


print(df) 

#Kayıp veriler 

print(df.isnull().sum())  

#Kayıp verileri başka verilerle doldurma 

df_filled=df.fillna(value={'Yaş':df['Yaş'].mean()}) 


#Kayıp verileri silme 

df_droped=df.dropna() 

#Veri seti birleştirme 

df2=pd.DataFrame({'isim':['Burak','Derya'],'Yaş':[30,25],
                 'sehir':['KONYA','TRABZON']})  

df_concat=pd.concat([df,df2],ignore_index=True) 
print(df_concat) 

df_merged=pd.merge(df,df2,on='isim',how='outer') 

df_filtered=df[(df['Yaş']>25) & (df['Şehir'].isin(['İSTANBUL','ANKARA']))] 


# VERİ SİLME

df.drop(columns='dogum tarihi',inplace = True) 

















































