# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:22:26 2018
#本代码创新点
'''
1.对loadDataSet函数进行了修改，使之更符合文本内容python3的环境
2.为了帮助确定最佳分类类别，添加了计算不同k值轮廓系数的函数，多次运行后确认该函数比较稳定
3.对结果的输出进行了优化，并且绘制了不同类别的散点图
4.此外，应用python的sklearn.cluster.KMeans函数对以上过程重新进行了实现，并对两种方法的结果进行了对比，
确认本文算法的正确性与准确性
注意：图形输出目前支持二维数据，三维及以上数据方法还未添加
'''
@author: xu
"""
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
 # 加载数据
def loadDataSet(fileName):  # 解析文件，按tab分割字段，得到一个浮点数字类型的矩阵
    dataMat = []
                # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        b=[]
        curLine = line.strip().split('')
#        curLine = line.strip().split('   ')
        for j in range(len(curLine)):            
            b.append(float(curLine[j]))
        dataMat.append(b)     
    return dataMat
 
 # 计算欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) # 求两个向量之间的距离
 
 # 构建聚簇中心，取k个(此例中为4)随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]#列数
    centroids = mat(zeros((k,n)))   # 每个质心有n个坐标值，总共要k个质心,
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)#只有矩阵才可以一列插入，np.array不可以
    return centroids
 
 # k-means 聚类算法
def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]#shape()，得出矩阵的行与列，[0]取行值
    clusterAssment = mat(zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
     # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k)
    clusterChanged = True   # 用来判断聚类是否已经收敛
    while clusterChanged:
        
        clusterChanged = False;
        for i in range(m):  
            # 把每一个数据点划分到离它最近的中心点
            minDist = inf; minIndex = -1;
            for j in range(k):
                
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            if clusterAssment[i,0] != minIndex: clusterChanged = True;  # 如果分配发生变化，则需要继续迭代
            clusterAssment[i,:] = minIndex,minDist**2   # 并将第i个数据点的分配情况存入字典,minDist的2次方
        for cent in range(k): # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去第一列等于cent的所有列
            #nonzero函数返回非零元素的目录,即index，类型是array元组，A表示返回值为cent的，
            #[0]返回nonzero结果的第一个，即index,拿出相应顺序的原始值
            centroids[cent,:] = mean(ptsInClust, axis = 0)  # 沿矩阵列方向进行均值计算,重新计算质心算
    return centroids, clusterAssment
#画图有两种方式，其一调用下面的函数showCluster1
def showCluster1(dataSet,k,clusterAssment):#无图例,为查证是否可用
    mark = ['Dr', 'Db', 'Dg', 'Dk','^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(shape(dataSet)[0]):
        num=int(clusterAssment[i,0])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[num])
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
#画图有两种方式，其而调用下面的函数showCluster2
def showCluster2(dataSet,k,clusterAssment):#有图例
    
    a=[]
    for i in range(k):
        a.append(dataSet[np.nonzero(clusterAssment[:,0].A==i)[0]].tolist())#矩阵转换为list
        print(i,'类：',dataSet[np.nonzero(clusterAssment[:,0].A==i)[0]])#打印不同类别的数据
    for j in range(k):
        plt.scatter(np.mat(a[j])[:,0],np.mat(a[j])[:,1],label=j+1)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
#k值的选择
def choice_k(mink,maxk,datMat):
    Silhouette=-2#最优轮廓系数
#    k=0#最优类别
    dic=[]
    for i in range(mink,maxk):#每个k
        myCentroids,clustAssing = kMeans(datMat,i)
        m = shape(datMat)[0]#数据数量
        Silhouette2=0#每个点的轮廓系数
        for j in range(m):#对每个数据，数据行
            type=clustAssing[j,0]#所属类别
            dattype=datMat[np.nonzero(clustAssing[:,0].A==type)[0]]#找到该类别的所有点
            numtype=shape(dattype)[0]
            L=0
            for k in range(numtype):#求组内的总距离
                L=distEclud(dattype[k,:],datMat[j,:])+L
            meanL=L/float(numtype)#float,组内距离均值
            meanother=np.inf#其他组的距离
            for ik in range(k):
                if ik!=type:
                    othdattype=datMat[np.nonzero(clustAssing[:,0].A==ik)[0]]#类别ik的所有点
                    numtypeik=shape(othdattype)[0]
                    if numtypeik>0:
                        L2=0
                        for other in range(numtypeik):
                            L2=distEclud(othdattype[other,:],datMat[j,:])+L2
                        meanL2=L2/float(numtypeik)
                        if meanL2<meanother:#选择距离组外各点距离均值最小的
                            meanother=meanL2
            if meanother>meanL:                
                Silhouette2=(meanother-meanL)/max(meanother,meanL)+Silhouette2    
        meanSilhouette=Silhouette2/float(m)#当分类i类时的轮廓系数
        dic.append([i,meanSilhouette])
        if meanSilhouette>Silhouette:
            Silhouette=meanSilhouette#选择最优轮廓系数，最大的
            besk_k=i
        
    return besk_k,Silhouette,dic

 # 用测试数据及测试kmeans算法
datMat =np.array(loadDataSet('testSet2.txt'))#mat函数可以将目标数据的类型转换为矩阵,<class 'numpy.matrixlib.defmatrix.matrix'>
k,Silhouette,dic=choice_k(2,8,datMat)#迭代运行多次取最优
di=np.mat(dic)

print('类别及轮廓系数',di)
print('最优分类类别数：',k,'最优轮廓系数：',Silhouette)  
myCentroids,clustAssing = kMeans(datMat,k)
print('各类中心：',myCentroids)#中心点
#print(clustAssing)
showCluster2(datMat,k,clustAssing)

#其实sklearn里面有现成的算法可以调用，调用过程如下，此方法不可与上共同运行
from sklearn.cluster import KMeans
import sklearn
datMat =np.array(loadDataSet('testSet2.txt'))
score_list = list()  # 用来存储每个K下模型的平局轮廓系数
silhouette_int = -1  # 初始化的平均轮廓系数阀值
for n_clusters in range(2, 10): # 遍历从2到10几个有限组
    model_kmeans =KMeans(n_clusters=n_clusters, random_state=0) # 建立聚类模型对象
    cluster_labels_tmp =model_kmeans.fit_predict(datMat)  # 训练聚类模型
    silhouette_tmp=sklearn.metrics.silhouette_score(datMat, cluster_labels_tmp) # 得到每个K下的平均轮廓系数
    if silhouette_tmp >silhouette_int:  # 如果平均轮廓系数更高
        best_k =n_clusters  # 将最好的K存储下来
        silhouette_int =silhouette_tmp  # 将最好的平均轮廓得分存储下来
        best_kmeans =model_kmeans  # 将最好的模型存储下来
        cluster_labels_k =cluster_labels_tmp  # 将最好的聚类标签存储下来
    score_list.append([n_clusters, silhouette_tmp])  # 将每次K及其得分追加到列表
estimator=KMeans(n_clusters=best_k)
a=estimator.fit(datMat)
b=label_pred = estimator.labels_ #获取聚类标签
c=centroids = estimator.cluster_centers_ #获取聚类中心
d=inertia = estimator.inertia_ # 获取聚类准则的总和
print ('{:*^60}'.format('K value and silhouette summary:'))
print (np.array(score_list)) # 打印输出所有K下的详细得分
print ('Best K is:{0} with average silhouette of{1}'.format(best_k, silhouette_int.round(4)))
print('聚类标签等',a,b,c,d)



