# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:13:42 2024

@author: itsme
"""

import seaborn as sns 
import pandas as pd 
import mathplotlib.pylot as plt 

#veri seti yükleme 
titanic=sns.load_dataset('titanic') 

sns.set_theme(style="darkgrid") 

sns.countplot(x="class", data=titanic,hue="sex", palette="Blues") 
plt.show()


sns.histplot(data=titanic, x="age", hue="sex", kde=True, bins=5) 
plt.show() 

sns.boxplot(data=titanic, x="class", y="age", hue="sex", palette="Greens") 
plt.show() 


sns.scatterplot(data=titanic, x="age", y="fare", hue="alive",palette="Greens")  

sns.jointplot(data=titanic, x="age", y="fare", hue="alive", palette="Greens") 


  
