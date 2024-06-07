# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:47:06 2024

@author: itsme
"""

import pandas as pd 
from sklearn import linear_model 

df=pd.read_csv("C:/Users/itsme/Downloads/cars.csv")    

df.info() 
x = df[["Weight","Volume"]]  
y = df["CO2"] 

dir(linear_model) 

model=linear_model.LinearRegression() 
model.fit(x,y) 

tahminCO2=model.predict([[3000,1000]]) 
print(tahminCO2) 

tahmin1CO2=model.predict([[1600,2000]]) 
print(tahmin1CO2) 

tahmin2CO2=model.predict([[1000,2000]]) 
print(tahmin2CO2) 

tahmin3CO2=model.predict([[1000,1000]]) 
print(tahmin3CO2) 



