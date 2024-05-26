# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:21:54 2024

@author: itsme
"""

"""
Passenger ID : Her bir yolcu için ayrı değer taşıyan ve Int64(Tamsayı) değerinde olan bir değişken.
Survıved : Ilgılı yolcunun hayatta kalıp kalmadığını gösterir. Float64 tipindedir.(1: Hayatta, 2 : Hayatta değil)
Pclass : Tamsayı değerli bir değişkendir ve yolcunun bilet sınıfını gösterir.
Name: Kategorik bir değişkendir. Yolcunun ismini gösterir.
Sex : Başka bir kategorik değişkendir. Yolcunun cinsiyetini gösterir.
Age : Float64 tipindeki değişken yolcunun yaşını gösterir.
Sibsp : İnt64 tipindeki değişken gemideki yolcunun kardeş ve eş sayısını gösterir.
Parch : İnt64 tipindedir ve yolcunun çocuk sayısını, ebeveyn sayısını gösterir.
Ticket : Kategorik değişken olak ticket değişkeni yolcunun bilet kodunu gösterir.
Fare : Tamsayı değerindeki fare değişkeni yolcunun bilete ödediği miktarı belirtir.
Cabin : Kategorik değişken olan cabin değişkeni yolcunun kabin numarasını gösterir.
Embarked: Son değişkenimiz olan embarked değişkeni kategorik bir değişken olup
 yolcunun gemiye binmiş olduğu güverte bilgisini taşır.
"""



import seaborn as sns 
import pandas as pd 

titanic=sns.load_dataset('titanic') 

print(titanic.head()) 

print(titanic.info()) 


survival_sex=titanic.groupby('sex')['survived'].mean() 
print(survival_sex) 

#yas

titanic['age'].fillna(titanic['age'].mean(), inplace=True)


# Yaş gruplarına göre veri setini bölme ve her grup için hayatta kalma oranını hesaplama

age_bins = [0, 18, 25, 40, 60, 80] # Yaş gruplarını tanımlama
age_labels = ['0-18', '19-25', '26-40', '41-60', '61-80'] 
titanic['age_group'] = pd.cut(titanic['age'], bins=age_bins, labels=age_labels) 


survival_age=titanic.groupby('age_group')['survived'].mean() 
print(survival_age) 


#Biniş limanına göre hayatta kalma oranlarını hesaplama 

survival_embark_town=titanic.groupby('embark_town')['survived'].mean() 
print(survival_embark_town)


# 'sibsp' (kardeş/eş sayısı) ve 'parch' (ebeveyn/çocuk sayısı) sütunlarını kullanarak yeni bir 'family_size' sütunu oluşturma
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

# Aile boyutuna göre hayatta kalma oranlarını hesaplama
survival_family_size = titanic.groupby('family_size')['survived'].mean()
print(survival_family_size)

















