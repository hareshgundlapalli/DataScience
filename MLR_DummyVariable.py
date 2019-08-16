# -*- coding: utf-8 -*-
"""
Created on 08/15/2019
Assignment on Multiple Linear Regression - Dummy Variables
Purpose: Create Dummy variables on categorical variable
Dataset: iris [builtin r]
3 categories
@author: Haresh
"""
import pandas as pd

iris1 = pd.read_csv('D:\\Documents - SSD\\iris.csv')
iris1.Species.value_counts()

#Option 1: insert new columns manually using map function of pandas using dicts

iris1["Species_setosa"] = iris1.Species.map({'setosa':1,'versicolor':0,'virginica':0})
iris1["Species_versicolor"] = iris1.Species.map({'setosa':0,'versicolor':1,'virginica':0})
iris1.head()

#Option 2: insert new columns using get_dummies in pandas, drops original column and first dummy variable, adding others.

iris1 = pd.read_csv('D:\\Documents - SSD\\iris.csv')
iris1.Species.value_counts()

iris1 = pd.get_dummies(iris1, columns=['Species'], prefix_sep='_', drop_first=True)
iris1.head()

#Option 3: using get_dummies and keeping the original column

iris1 = pd.read_csv('D:\\Documents - SSD\\iris.csv')
iris1.Species.value_counts()

iris1 = pd.concat([iris1, pd.get_dummies(iris1.Species, prefix='Species').iloc[:,:-1]], axis=1)
iris1.head()
