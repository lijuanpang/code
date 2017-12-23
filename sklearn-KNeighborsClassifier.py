# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:30:59 2017

@author: xu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
x_train=np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
y_train=np.array(['love','love','love','action','action','action'])
knn=KNeighborsClassifier()
a=knn.fit(x_train,y_train)
print(a)
x_test=np.array([18,90])
b=knn.predict(x_test)
print(b)
