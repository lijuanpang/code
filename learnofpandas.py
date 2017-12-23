# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:49:37 2017

@author: xu
"""
import pandas as pd
import numpy as np
#pandas 两大核心数据结构是Series（一维）,DataFrame(多维).
#series一维数组，两个，一个用于存放各种类型 的数据，一个用来存放与之相关的标签，储存在另一个Index的数组中s

s = pd.Series([12,1,7,9])#values,把存放哎series对象中的数据以数组形式传入。左边Index并未指定,从0开始
#print(s)
s1 = pd.Series([12,-4,7,9],index=['a','b','c','d'])

#返回索引值最小和最大的元素下标
'''
print(s1)
print(s1.idxmin())
print(s1.idxmax())
'''
'''
print(np.argwhere(s1==12))#索引下标
print(s1)
print(s1.values)#查看值
print(s1.index)#查看标签
print(s1[2])#指定位置
print(s1['b'])#指定位置
print(s1[0:2])#取多项
print(s1[['a','b']])#这里有两个【】【】
#两种赋值方法
s1[0]=0
print(s1)
s1['b']=1
print(s1)

#两种方法定义Series对象,是对他们的引用，而不是复制，若原对象改变，那么也会随着变
arr=np.array([1,2,3,4])
s3=pd.Series(arr,index=['a','b','c','d'])
#print(s3)
s4=pd.Series(s)
arr[0]=7
#print(s3)

#筛选元素
print(s[s>8])

#对象运算和数学函数（和数组 的运算一样）
print(s/2)
print(np.log(s))#数学函数应该指明出处
'''
#series对象包含重复的元素，去重以及重复次数，所属关系
'''
serd=pd.Series([1,2,5,2,9,5],index=['white','white','yellow','pink','pink','black'])#里面的对象重复
s5=serd.unique()#返回的数组包含去重后的元素
s6 = serd.value_counts()#返回去重后的元素并附上重复的次数
print(serd.index.is_unique)#数据结构中是否存在重复的索引项
#print(s6)
s7=serd.isin([1,2])#isin可以判断所属关系，一列元素是否包含在数据解耦之中，返回布尔值
'''
#NaN
'''
s2 = pd.Series([5,-2,np.NaN,14])#为数组中元素缺失的项输入
#print(s2)
#isnull
#print(s2.isnull())#用来识别没有对应元素的索引
#print(s2.notnull())#同上
print(s2[s2.notnull()])#筛选不为0的数据
'''
#Series用作字典
'''
mydict={'red':2000,'blue':1000,'yellow':500,'orange':1000}
myseries=pd.Series(mydict)
#print(myseries)
myseries1=pd.Series(mydict,index=['red','yellow','orange','blue','green'])#通过识别标签对齐不一致的数据
#print(myseries1)
mydict2={'red':400,'yellow':1000,'black':700}
myseries2=pd.Series(mydict2)
myseries3=myseries+myseries2#两个对象相加，共同的元素求和，不同的元素为NaN
#print(myseries3)
'''
#DataFrame对象，与excel的表格相似，按一定顺序排列的多列数据，各列数据类型可以不同；两个索引index，
#常用方法是传递一个dict对象给DataFrame()构造函数
'''
data={'color':['blue','green','yellow','red','white'],'object':['ball','pen','pencil','paper','mug'],'price':[1.2,1.0,0.6,0.9,1.7]}
frame=pd.DataFrame(data)#方法一
print(frame)

#print(frame)
frame2=pd.DataFrame(data,columns=['object','price'])#选取dict对象中用到的数据，columns
#print(frame2)
frame3=pd.DataFrame(data,index=['one','two','three','four','five'])#自动添加index,
#print(frame3)
#方法二
frame4=pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','green','black'],columns=['ball','pen','pencil','paper'])
#print(frame4)
#方法三：用嵌套字典生成对象
nestdict={'red':{2012:22,2013:33},'white':{2011:13,2013:22,2013:16},'blue':{2011:17,2012:27,2013:18}}
frame5=pd.DataFrame(nestdict)
#print(frame5)
'''
#选取元素
'''
print(frame.columns)#列出所有列的名称
print(frame.index)#获取索引列表
print(frame.values)#获取所有的元素
print(frame['price'])#获取一列的内容：第一种方法
print(frame.ix[2])#获取其中的行，用ix属性和行的索引值就能获取
s=frame.ix[[2,4]]#选取多行
#print(s)
print(frame[0:2])#抽取多行的数据
print(frame['object'][0])#获取单个元素，依次指定元素所在的列名称，行的索引值或标签
'''
#赋值,按照元素获取的方法来进行赋值
'''
frame.index.name='id'
frame.columns.name='item'
frame['new']=[1,2,3,4,5]#添加新的一列，和索引是一样的，若想更新一列，需要把一个数组赋给这一列
a=np.arange(2,7)
frame['new']=a#修改一列。
frame['new'][1]=3#修改某个元素
print(frame)
'''
#元素的所属关系
'''
print(frame.isin([1.0,'pen']))#
print(frame[frame.isin([1.0,'pen'])])#将上述结果作为条件，得到新的，其中只包含满足条件的元素
'''
#删除一列
'''
del frame['color']
frame['color']=['blue','green','yellow','red','white']
print(frame)
'''
#筛选
'''
print(frame[frame<1.0])
'''
#转置
#frame51=frame5.T#行列交换
#print(frame51)
#索引一个标签对应多个元素，返回的是一个对象
'''
ser = pd.Series([2,3,4,5,4,5],index=['red','blue','black','oran','blue','black'])
'''
#print(ser['black'])
#frame.index.is_unique
'''
print(frame.index.is_unique)#与serd一样，判断是否存在重复的索引项
'''
#更换索引
'''
ser0=pd.Series([2,5,7,4],index=['one','two','three','four'])
#ser0.index=['1','2','3','4']#方法一
ser0.reindex(['three','four','five','one'])#更换索引，调整索引序列中各标签的顺序，删除或增加，不存在的标签元素添加为NaN
#print(ser0.reindex(['three','four','five','one']))#产出了two,增加了five
#重新编制索引，自动填充或插值法

ser1 = pd.Series([1,5,6,3],index=[0,3,5,6])
ser10=ser1.reindex(range(6),method='ffill')#添加缺失的索引项，新插入的索引项，其元素为前面索引号比它小的那个元素
ser11=ser1.reindex(range(6),method='bfill')#添加的索引项，其元素为后面的元素
#print(ser11)
frame0=frame.reindex(range(5),method='ffill',columns=['color','object','price','new'])
#print(frame0)
'''
#删除drop()，返回不包含已删除索引及其元素的新对象
#Series
'''
ser=pd.Series(np.array([1,2,3,4]),index=['red','blue','yellow','white'])
#print(ser)
ser00=ser.drop(['red'])#drop('red')
ser01=ser.drop(['red','blue'])
print(ser01)

#DataFrame
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame0=frame.drop(['red','blue'])#删除行
frame1=frame.drop(['ball','pen'],axis=1)#删除列，指定轴
print(frame1)
'''
#算数和数据对齐
'''
s1=pd.Series([3,2,5,1],index=['white','yellow','green','blue'])#加运算，对齐
s2=pd.Series([1,4,7,2,1],index=['white','yellow','black','blue','brown'])
#print(s1+s2)
frame1=pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame2=pd.DataFrame(np.arange(12).reshape(4,3),index=['blue','green','white','yellow'],columns=['mug','pen','ball'])
#print(frame1+frame2)
s3=pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
#print(frame1)
#print(s3)
frame1s=frame1.sub(s3)#frame-Series,一定矩阵在前，colums=index
s3['mug']=9
#print(s3)
frame1s2=frame1.sub(s3)#如果索引项只存在其中一个数据结构之中，则运算结果会为该索引项生成一项，但数值为NaN
#print(frame1s2)

frame12=frame1.add(frame2)#相加
frame13=frame1.sub(frame2)#相减
frame14=frame1.div(frame2)#相除
frame15=frame1.mul(frame2)#相乘
#print(frame15)
'''
#pandas 库函数
#通用函数
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame0=np.sqrt(frame)#使用通用函数

#print(frame0)
#自定义函数
'''
f1=lambda x:x.max()-x.min()#定义函数的两种方法
def f2(x):
    return x.max()-x.min()#这样返回的是一个标量
frame.apply(f1)#自动默认Wie是列的运算
frame.apply(f2,axis=1)#变成行内的运算

#自定义函数返回一个Sries对象，可执行多个函数
def f3(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
#print(frame.apply(f3))
'''
#统计函数，多数统计函数对Dataframe对象有效，故可以不适用apply函数
'''
frame.sum()
frame.mean()#默认为按列运算
frame.describe()#可描述多个统计量
'''
#排序和排位次，pandas的sort_index（）返回一个和原对象元素相同但顺序不同的新对象
'''
ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])#默认升序，按照index
print(ser)
ser1=ser.sort_index()
ser2=ser.sort_index(ascending=False)#降序排列
ser3=ser.sort_values()#按values值升序
ser4=ser.sort()#不是很懂
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame1=frame.sort_index()#默认是按行排列，也就是index
frame2=frame.sort_index(axis=1)#按列排序，就是columns
#对元素进行排序
ser5=ser.order()
frame3=frame.sort_index(by='pen')#指定根据那一列的元素进行排列
frame4=frame.sort_index(by=['pen','pencil'])#基于两列或更多的列进行排序
#排位次操作，数值从小到大，越靠前数值越小
ser6=ser.rank()#默认升序
ser7=ser.rank(ascending=False)#降序
#print(ser6)
#print(frame3)
'''
#相关性和协方差corr（），cov（）通常涉及两个Series对象 
'''
seq2=pd.Series(np.array([3,4,3,4,5,4,3,2]),index=['2006','2007','2008','2009','2010','2011','20112','2013'])
seq=pd.Series(np.array([1,2,3,4,4,3,2,1]),index=['2006','2007','2008','2009','2010','2011','20112','2013'])
seq.corr(seq2)
seq.cov(seq2)
#计算单个dataframe对象的相关性和协方差，返回两个新的dataframe对象形式矩阵
frame=pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame.corr()
frame.cov()
#print(frame.corr())
#corrwith()可以计算dataframe对象的列或行与Series对象或其他dataframe对象元素两两之间的相关性
frame2=pd.DataFrame(np.arange(12).reshape(4,3),index=['blue','green','white','yellow'],columns=['mug','pen','ball'])
ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
frame.corrwith(frame2)#两个
frame.corrwith(ser)#一个dataframe，一个series
'''
#NaN数据
'''
#为数据结构中的元素赋NaN，用numpy的np.NaN
ser=pd.Series([0,1,2,np.NaN,9],index=['red','blue','yellow','white','green'])
ser['white']=None
#去除NaN的方法，dropna()
ser1=ser.dropna()#直接过滤方法一
ser2=ser[ser.notnull()]#筛选过滤方法二
#对于Dataframe，如果用dropna()，那么只要有一行或一列有该元素，整行或整列都会被删除，故用
frame=pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],index=['blue','green','red'],columns=['ball','mug','pen'])
frame1=frame.dropna(how='all')#告知dropna函数只删除所有元素均为nan的行或列,是行
frame2=frame.dropna(how='all',axis=1)#是删除全部为nan的列
#过滤有风险，所以对于nan可以用其他的数来代替，用fillna()可以替换所有nan的元素
frame3=frame.fillna(0)
print(frame3)
'''
#等级索引和分级，多级数据，两层的数据结构
'''
mser=pd.Series(np.random.rand(8),index=[['white','white','white','blue','blue','red','red','red'],['up','down','right','up','down','up','down','left']])
mser.index#指定等级索引，二级元素的选取操作得以简化
mser['white']#一层列表选取,第一列索引中某一索引项的元素
mser[:,'up']#选取第二列索引中某一索引项的元素
mser['white','up']#选取某一特定的元素，指定两个索引项即可
#使用unstack()可以把Series转成dataframe
frame2=pd.DataFrame(np.arange(12).reshape(4,3),index=['blue','green','white','yellow'],columns=['mug','pen','ball'])
frame2.stack#把dataframe转成series
mser.unstack()#把series转成dataframe
#二级索引dataframe
mframe=pd.DataFrame(np.random.rand(16).reshape(4,4),index=[['white','white','red','red'],['up','down','up','down']],columns=[['pen','pen','paper','paper'],[1,2,1,2]])
#print(mframe)
'''
#层级排序与重新调整顺序
'''
mframe=pd.DataFrame(np.random.rand(16).reshape(4,4),index=[['white','white','red','red'],['up','down','up','down']],columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe.index.names=['colors','status']
mframe.columns.names=['object','id']
mframe.swaplevel('colors','status')#互换index中的两个层级名称
mframe.sortlevel('colors')#只根据color排序
#对行一层级进行统计，把层级的名称赋给level即可,默认是行
mframe.sum(level='status')
print(mframe.sum(level='object',axis=1))#数据列

#print(mframe)

'''
mser=pd.Series(np.random.rand(8),index=[['white','white','white','blue','blue','red','red','red'],['up','down','right','up','down','up','down','left']])
#print(mser,type(mser))
mframe=pd.DataFrame(np.random.rand(16).reshape(4,4))
mfr=np.array(mframe)
print(type(mfr))