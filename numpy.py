#map(),下文是一个迭代器
'''
def f(x):
    return x+1
print(map(f,[1,2,3]))

L=['adam', 'LISA', 'barT']
def rules(str):
   return str[0].upper()+str[1:].lower()
print(map(rules,L))
map_list=[item for item in map(rules,L)]

L0=list(map((lambda str:str[0].upper()+str[1:].lower()),['adam', 'LISA', 'barT']))
print(L0)
'''
#filter()
'''
def is_odd(x):
    return x%2==1
print(filter(is_odd,[3,2,1]))
filter_list=[item for item in filter(is_odd,[3,2,1])]
print(filter_list)

L1=list(filter((lambda x:x%2==1),[1,2,3,4]))
print(L1)
'''
#reduce()
'''
from functools import reduce
sum = reduce((lambda x,y:x+y),(1,2,3,4))
print(sum)
'''
#数组的维数和元素数量由数组的型来决定，数组的型由N个正整数组成的元组来指定，元组每个元素对应每一维的大小，
#数组的维是轴，轴的数量是秩
import numpy as np
'''
a = np.array([1,2,3])
print(a)
print(type(a))#检测新创建的对象是否是ndarray
print(a.dtype)#获知新建的ndarray属于哪种数据类型
print(a.ndim)#轴数量（维）
print(a.size)#数组长度
print(a.shape)#数组的型

#2*2维数组
b = np.array([[1.3,2.4],[0.3,4.1]])
print(b.dtype)
print(b.ndim)
print(b.size)
print(b.shape)
print(b.itemsize)
print(b.data)
'''
#创建数组的方法
'''
c = np.array([[1,2,3],[4,5,6]])#方法一
print(c)
d = np.array([(1,2,3),(4,5,6),[7,8,9]])#方法二
print(d)
e = np.array(((1,3,2),(4,6,5)))#方法三
print(e)
g = np.array([['a','b'],['c','d']])#字符串类型等
#print(g)
print(g.dtype)
print(g.dtype)

f = np.array([[1,2,3],[4,5,6]],dtype=complex)#指定数组类型为复数
print(f)
g = np.zeros((3,3))#生成3*3的二维数组
print(g)
h = np.ones((3,3))
print(h)
i = np.arange(1,10)
print(i)
i0 = np.arange(0,10,3)#有间隔为3的数字，第三个参数也可以是浮点数，比如0.3
print(i0)

i1 = np.arange(0,12).reshape(3,4)#用arange创建多维数组
print(i1)
j = np.linspace(0,10,5)#第三个参数表示把俩个数字之间的范围分为几部分,包括10
print(j)
'''
#数组的基本操作
'''
a = np.arange(4)
print(a+4,a*2)
a +=1#a自加1而不产生新的数组
print(a)
a *=2#a自乘2而不产生新的数组
print(a)

#两个数组相加，是数组中相同位置相加
b = np.arange(4,8)
print(a+b,a*b,a*np.sin(b))

A=np.arange(0,9).reshape(3,3)#对于多维数组，依然是相同位置的元素相乘
B=np.ones((3,3))
print(A*B)
print(np.dot(A,B))#矩阵积第一种方法
print(A.dot(B))#矩阵积第二种方法把dot()函数当做其中一个矩阵对象的方法
'''
#通用函数是对数组里面的每个元素进行计算，sqrt,sin,cos
'''
a = np.arange(1,5)
print(np.sqrt(a))
'''
#聚合函数，索引
'''
a = np.array([1,2,3,4])
b=[3,4,6,5]
print(b.index(3))#list索引下标
print(np.argwhere(a==2))#array索引下标

print(a[3])#索引机制，直接输入下标
print(a[[1,2]])#索引多个下边数据，两个【】
print(a.sum())
print(a.min())
print(a.max())
print(a.mean())
print(a.std())#计算沿指定轴的标准偏差
a = np.arange(0,12).reshape(3,4)
print(a[0,0])#取第一行第一列数字
'''
#切片+数组迭代
'''
a = np.arange(10,16)
#print(a)
#print(a[2:5])#抽取
#print(a[1:5:2])#每隔两个抽取一个
A = np.arange(10,19).reshape(3,3)
#print(A)
#print(A[0,:])#只抽取第一行
#print(A[0:2,0:2])#抽取一个小点儿的矩阵
#print(A[[0,2],0:2])#抽取的行不连续，这里0:2是前两列

for row in A:
    print(row)#遍历矩阵
for item in A.flat:
    print(item)#遍历每个元素

#用聚合函数处理每一行或列，返回一个数值作为结果：apply_along_axis()，聚合函数，对那条轴
print(np.apply_along_axis(np.mean,axis=0,arr=A))#axis为0是按列进行迭代，得出每一列的平均数
print(np.apply_along_axis(np.mean,axis=1,arr=A))#按行,其中第一个参数函数可以自己定义
'''
#条件和布尔 形状改变，矩阵转置
'''
A = np.random.random((4,4))#0-1之间的随机数
#print(A)
#print(A<0.5)
B = A[A<0.5]#选取符合条件的组成新的数组
#print(B)
a = np.random.random(12)#12个0-1之间的随机数
#print(a)
a1=a.reshape(3,4)
#print(a1)
a2=a1.ravel()#从二维转为一维
#print(a2)
a3=a1.transpose()
print(a3)#矩阵转置
'''
#连接数组，
'''
A = np.ones((3,3))
B = np.zeros((3,3))
C =np.vstack((A,B))#垂直入栈，把第二个数组作为行添加到第一个数组中
D = np.hstack((A,B))#水平入栈，作为列添加
#print(C)
#print(D)
a = np.array([0,1,2])
b = np.array([3,4,5])
c = np.array([6,7,8])
d = np.column_stack((a,b,c))#每个都为列
e = np.row_stack((a,b,c))#每个都作为行
print(d)
print(e)
'''
#数组切分，水平切分：hsplit(),垂直切分：vsplit()
'''
a = np.arange(16).reshape((4,4))
print(a)
[b,c] = np.hsplit(a,2)
#print(b,c)
[d,e] = np.vsplit(a,2)#将高度截一半
#print(d,e)
#split索引，分成不对称的几个部分，axis为1是列索引，axis为0是行索引
[a1,a2,a3]=np.split(a,[1,3],axis=1)#列索引，切为三部分
#print(a1,a2,a3)
[a4,a5,a6]=np.split(a,[1,3],axis=0)#行索引
#print(a4,a5)
'''
#对象的副本或视图
'''
a = np.array([1,2,3,4])
c = a.copy()#生成一份完整的副本，从而得到不同的数组
a[0]=0
print(c)
'''
#结构化数组，包含的是结构或记录而不是元素
'''
name=['alice','bob','cathy','doug']
age=[25,45,37,19]
weight=[55,86,78,51]
x = np.zeros(4,dtype=int)
data=np.zeros(4,dtype={'names':('name','age','weight'),'formats':('U10','i4','f8')})
#print(data.dtype)
data['name']=name
data['age']=age
data['weight']=weight
#print(data)
#print(data['name'])
#print(data[0])
structured=np.array([(1,'first',0.5,1+2j),(2,'second',1.3,2-2j),(3,'third',0.8,1+3j)],dtype=('int16,a6,float32,complex64'))
#print(structured)#上式中的第三个必须是方括号（）
#print(structured[0])
#print(structured['f1'])#f0,f1,f2'是自动赋给结构体每个元素的名称可以看成是数组列的名称

#指定名称
struc1=np.array([(1,'first',0.5,1+2j),(2,'second',1.3,2-2j),(3,'third',0.8,1+3j)],dtype=[('id','i2'),('position','a6'),('value','f4'),('complex','c8')])
print(struc1['id'])
#或在创建后，重新定义结构化数组的dtype属性，指定各字段名称
#sturc.dtype.names=('id','order','value','complex')
'''
#二进制文件读写
'''
a = np.arange(16).reshape(4,4)
np.save('F:/python3/a.npy',a)
loaded_data=np.load('F:/python3/a.npy')
print(loaded_data)
'''
#从文本文件中读取，csv
'''
data1=np.genfromtxt('F:/python3/haha.csv',delimiter=',',names=True)
#print(data1)
print(data1['id'])
'''



