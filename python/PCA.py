# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:39:02 2017

@author: xu
"""
#主城成分分析（PCA），常用降维方法，常用于高维数据集的探索与可视化，还可用户数据压缩和预处理
                                                                    '''
可将具有相关性的高维变量合成为线性无关的低维变量，成为主成分，可以尽可能保留原始数据的信息
方差：离散程度；协方差：两个变量之间的线性相关性程度；特征向量：描述数据集结构的非零向量
原理：矩阵的主成分就是其协方差矩阵对应的特征向量，按照对应的特征值大小进行排序， 最大的特征值就是第一主成分
sklearn 中，可以使用sklearn.decomposition.PCA进行降维，主要参数：
n_components:指定主成分的个数
svd_solver:设置特征值分解的方法，默认为’auto‘,其他可选为’full‘,'arpack','randomized'
'''
#数据，萼片长度，萼片宽度，花瓣长度，花瓣宽度四列
'''
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
data=load_iris()
y = data.target#使用y表示数据集中的标签，主要是0,1,2
x = data.data#使用x表示数据集中的属性数据，四列数据
pca = PCA(n_components=2)#加载pca算法，设置降维后主成分个数
reduced_x = pca.fit_transform(x)#对原始数据进行降维，并保存
#按类别对降维后的数据进行保存
red_x,red_y = [],[]#第一类数据点
blue_x,blue_y = [],[]#第二类数据点
green_x,green_y = [],[]#第三类数据点
for i in range(len(reduced_x)):
    if y[i] ==0:
        red_x.append(reduced_x[i][0])
        red_x.append(reduced_y[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_y[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])
        
plt.scatter(red_x,red_y,c = 'r',marker='x')
plt.scatter(blue_x,blue_y,c = 'b',marker='D')
plt.scatter(green_x,green_y,c = 'g',marker='.')
'''
#非负矩阵分解（NMF）：是在矩阵中所有元素均为非负数约束条件之下的矩阵分解方法。
#基本思想：给定一个非负矩阵V，NMF能够找到一个非负矩阵W和一个非负矩阵H，使得矩阵W和H的乘机近似等于矩阵V中的值。

#










                           