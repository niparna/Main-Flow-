# -*- coding: utf-8 -*-
"""Task5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rtxqUWh3QBHrrXtdDThPdhV9xVfOlC2o
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/heart.csv')

df.head()

df.tail()

df.isnull().sum()

df.hist(bins=50,figsize=(20,15),grid=False)

df.describe()

df.target.value_counts()

df.target.value_counts().plot(kind='bar')
plt.title('Heart Disease')
plt.xlabel('1= Heart Disease, 0=No Heart Disease')
plt.ylabel('Amount')
plt.show()

df.target.value_counts().plot(kind='pie')
plt.legend()

pd.crosstab(df.target,df.sex)

sns.countplot(x='target',hue='sex',data=df)
plt.xlabel('0=No Heart Disease, 1= Heart Disease')
plt.ylabel('Amount')
plt.show()

df.cp.value_counts().plot(kind='bar')
plt.title('Chest Pain Type VS Count')

pd.crosstab(df.sex,df.cp)

pd.crosstab(df.sex,df.cp).plot(kind='bar')
plt.title('Type Chest Pain for sex ')
plt.xlabel('0 = Female,  1 = Male')
plt.show()

pd.crosstab(df.cp,df.target)

sns.countplot(x='cp',hue='target',data=df)

sns.displot(x = 'age', data = df, kde = True, bins = 30)

sns.displot(x = 'thalach', data = df, kde = True, color='green', bins = 30)