# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:41:34 2017

@author: xu
"""
#本章数据准备，数据转换数据聚合
#数据准备阶段：加载，组装（合并，拼接，组合），变形，删除
import pandas as pd
import numpy as np
'''
python的组装方法有：合并（pandas.mege()）根据一个或多个键连接多行，join操作；
拼接（pandas.concat()）函数按照轴把多个对象拼接起来
结合：pandas.DataFrame.combine_first()函数从一个结构中获取数据，连接重合的部分，以填充缺失值
'''
#合并
'''
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],'price':[12.33,11.44,33.21,13.23,33.62]})
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],'corlor':['white','red','red','black']})
frame12=pd.merge(frame1,frame2)#根据id中元素共同的进行合并连接，
print(frame2)#返回的dataframe对象由原来两个dataframe对象中ID相同的行组成，除了id这一列，新的对象还包括原来分属于两个dataframe的其他列

frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],'corlor':['white','red','red','black','green'],'brand':['OMG','ABC','ABC','POD','POD']})
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],'brand':['OMG','POD','ABC','POD']})
frame12=pd.merge(frame1,frame2)#两个dataframe有两个相同的标签，所以合并时得到的是空集
#定义pandas合并操作所遵循的标准，用on选项指定合并操作所依据的基准列
frame121=pd.merge(frame1,frame2,on='id')#标准列是'id'
frame122=pd.merge(frame1,frame2,on='brand')#标准列是‘brand’
#print(frame122)

frame2.columns=['brand','sid']#重新指定columns
frame121=pd.merge(frame1,frame2,left_on='id',right_on='sid')#将两个列名不一样的列连接在一起，frame1的id列与frame2的sid列对应合并
#merge()函数默认执行的是内连接操作，上述结果中的键是交叉操作得到的
print(frame121)
'''
#外链接,左连接，右连接。外连接：把所有的键整合到一起，相当于左连接和右连接的效果之和，连接类型用how确定
'''
frame123=pd.merge(frame1,frame2,on='id',how='outer')#外连接将两个对象中所有的数据都连接列出，对于部分没有选项的置为NAN
print(frame123)
#左连接和右连接与外连接类型，how
frame124=pd.merge(frame1,frame2,on='id',how='left')#左连接以左边对象的元素为主，如果左边元素有，右边没有，那么将右边相应的项置为NAN
#print(frame124)
frame125=pd.merge(frame1,frame2,on='id',how='right')
print(frame125)
print(frame121)
'''
#合并多个键，把多个键赋给on选项
'''
frame126=pd.merge(frame1,frame2,on=['id','brand'],how='outer')#先根据第一对象的id和brand列出，对象2中相应的为nan,后根据第二对象的列出
print(frame126)
'''
#根据索引合并:用right_index=True,left_index=True将其激活
'''
frame127=pd.merge(frame1,frame2,right_index=True,left_index=True)#纯粹按照共同存在索引，显示出两对象中所有的列
#但join（）函数更适合根据索引进行合并，还可以用它合并多个索引相同或索引相同但列不一致的对象
frame2.columns=['brand2','id2']#使用join时两个对象中不能有名字相同的列，比如'id',所以要改掉
frame128=frame1.join(frame2)#连接时是按照索引值最大的对象列出索引，然后将索引值小的对象部分列表置为空
print(frame128)
'''
#数据拼接，numpy的concatenate()可用于数组的拼接操作
#数组的拼接
'''
array1=np.array([[0,1,2],[3,4,5],[6,7,8]])
array2=np.array([[6,7,8],[9,10,11],[12,13,14]])
array3=np.concatenate([array1,array2],axis=1)#横着拼接，两个数组的第一行横向组合
array4=np.concatenate([array1,array2],axis=0)#纵向拼接，第二个数组按列排在第一个数组的下面
#print(array3)
#pandas库以及它的Series和DataFrame等数据结构实现了带编号的轴，扩展数组拼接功能，pandas的concat()函数实现了按轴拼接的功能
ser1=pd.Series(np.random.rand(4),index=[1,2,3,4])
ser2=pd.Series(np.random.rand(4),index=[5,6,7,8])
ser3=pd.concat([ser1,ser2])#按列拼接，默认按照axis=0；返回Series对象
#外连接操作拼接concat()
ser4=pd.concat([ser1,ser2],axis=1)#返回的dataframe对象，横向拼接变成两列，默认列名是（0，1）,为空的元素用nan代替
#内连接操作，用join选项设置为inner
ser5=pd.concat([ser1,ser3],axis=1,join='inner')#内连接是连接索引有重合部分的数据，ser3,无法识别被拼接的部分
#在用于拼接的轴上创建等级索引，借助keys来实现
ser6=pd.concat([ser1,ser2],keys=[1,2])
ser7=pd.concat([ser1,ser2],axis=1,keys=[1,2])#dataframe对象，keys成为列名

#dataframe的拼接方法与之相同
frame1=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[1,2,3],columns=['A','B','C'])
frame2=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[4,5,6],columns=['A','B','C'])
frame3=pd.concat([frame1,frame2])#默认是按列拼接,不会去除索引相同的数据
frame4=pd.concat([frame1,frame2],axis=1)#默认是按行拼接,空的数值用nan
print(frame1)
print(frame2)
#print(ser4)
print(frame3)
'''
#组合：当两个数据集的索引完全或部分重合时，无法用合并和拼接方法组合数据
'''
ser1=pd.Series(np.random.rand(5),index=[1,2,3,4,5])
ser2=pd.Series(np.random.rand(4),index=[2,4,5,6])
ser3=pd.concat([ser1,ser2])
ser4=ser1.combine_first(ser2)#该组合已经去除了索引重合的数据
ser5=ser2.combine_first(ser1)
ser6=ser1[:3].combine_first(ser2[:3])
print(ser6)
#print(ser4)
#print(ser3)
'''
#轴向旋转:入栈（sracking）把列转化为行，出栈（unstacking）是把行转换为列,变成series对象
'''
frame1=pd.DataFrame(np.arange(9).reshape(3,3),index=['white','black','red'],columns=['ball','pen','pencil'])
frame2=frame1.stack()#转变为具有二级索引的Series对下那个
frame3=frame2.unstack()#把列变成行，就是列的一级索引变成行
frame4=frame3.unstack()#把行变成列，就是行的索引变成一级索引
frame5=frame2.unstack(0)#把列的二级索引变成行名
print(frame2)
print(frame3)
print(frame5)
'''
#从长格式向宽格式旋转,增强数据的可读性
'''
longframe=pd.DataFrame({'color':['white','white','white','red','red','red','black','black','black'],
'item':['ball','pen','mug','ball','pen','mug','ball','pen','mug'],
'value':np.random.rand(9)})#数据可读性差，并且不能作为主键，因为主键要求是唯一的
#使用dataframe中的pivot（）函数将其转化为宽格式
wideframe=longframe.pivot('color','item')#color是第一主键，item是第二主键
print(longframe)
print(wideframe)
'''
#删除：数据处理的最后一步是删除多余的列和行
'''
frame1=pd.DataFrame(np.random.rand(9).reshape(3,3),index=['white','black','red'],columns=['ball','pen','pencil'])
#删除一列，del,指定列名
frame2=frame1.copy()#使用这个方法可以保留原对象
del frame1['ball']#直接在frame中删除一列，而不生成新的dataframe对象
#删除多余的行用drop（），将索引的名称作为参数
frame4=frame2.drop('white')#注意与del 的用法完全不同，drop是删除行时生成另一个dataframe对象，而本身不变，所以不同copy
print(frame2)
print(frame4)
'''
#数据转换6.3第二步，调整过数据的形式和结构之后，接下来就是数据转换
#6.3.1删除重复元素
'''
dframe=pd.DataFrame({'color':['white','white','red','red','white'],'value':[2,1,3,3,2]})
#dataframe中的duplicated()函数可用来检测重复的行，返回元素为布尔型的series对象，每个元素对应一行，若该行与其他行重复，则为T入耳，否则是False
dframe1=dframe.duplicated()
dframe2=dframe[dframe.duplicated()]#返回重复的元素
#通常所有重复的行都需要删除，pandas库的drop_duplicates()可实现删除功能，并返回删除重复行后的dataframe对象
dframe4=dframe.drop_duplicates()#返回去重之后的dataframe对象
dframe5=dframe.drop(0)#是索引的名称，所以是0,1，等
print(dframe5)
'''
#映射#pandas提供了相关函数，映射个庴就是黄创建一个映射关系列表，把与安娜苏跟一个特定的标签或字符串绑定起来
#定义映射关系，最好的对象是dict
map={'label1':'value1','label2':'value2'}
#接下来的函数都以表示映射关系的dict对象作为参数：replace（）：替换函数；map（）：新建一列；rename（）：替换索引
#用映射替换元素
'''
frame=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],'color':['white','rosso','verde','black','yellow'],'price':[5.56,4.20,1.30,0.56,2.75]})
print(frame)

frame1=frame.copy()
frame1['color'][1]='red'#不用映射时，这样也可以替换单个元素
#用新元素替换不正确的元素，需定义一组映射关系，旧元素作为键，新元素作为值
newcolors={'rosso':'red','verde':'green'}
frame2=frame.replace(newcolors)#传入表示映射关系的字典作为参数,结果已替换,并生成新的对象
frame3=frame.replace('rosso','red')#结果已替换，新对象
#还可以把nan替换为其他值，比如0，任然可用replace（）函数
ser=pd.Series([1,3,np.nan,4,6,np.nan,3])
ser_nan={np.nan:0}
ser1=ser.replace(ser_nan)#可以替换方法一
ser2=ser.replace(np.nan,0)#可以替换方法二
#print(ser2)
print(frame)
'''
#添加元素用映射
'''
frame=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],'color':['white','red','green','black','yellow']})
#下面的price是数组，而不是dataframe
price={'items':['ball','mug','bottle','scissors','pen','pencil','ashtray'],'price':[5.56,4.2,1.3,3.41,1.3,0.56,2.75]}
#需要用下面这个才会映射
price1={'ball':5.56,'mug':4.2,'bottle':1.3,'scissors':3.41,'pen':1.3,'pencil':0.56,'ashtray':2.75}#多于要增加的元素没关系，会从中拿出需要的几项
frame['price']=frame['item'].map(price1)
#print(frame)
print(price)
'''
#重命名索引轴:rename()函数，以表示映射关系的字典对象作为参数，替换轴的索引标签
#离散化和面元划分
'''
frame=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],'color':['white','rosso','verde','black','yellow'],'price':[5.56,4.20,1.30,0.56,2.75]})
reindex={0:'first',1:'second',2:'third',3:'fourth',4:'fifth'}
frame1=frame.rename(reindex)
frame2=frame.reindex([1,2,3,4,5])#这样也可以呀
#重新命名列，columns=dict
recolumns={'item':'objet','price':'value'}
frame3=frame.rename(columns=recolumns)
#一起重命名
frame4=frame.rename(index=reindex,columns=recolumns)
#对于单个赋值的情况，可以直接对传入的参数进行限定，而不用传入整个dict
frame5=frame.rename(index={1:'first'},columns={'price':'value'})
#frame6=frame.rename(columns={'item':'object1'},inplace=True)#加入inplace后，是直接在原frame上进行修改
#print(frame)

#6.4 离散化和面元划分：离散化数据转换过程，将元素分为几个类别，分析每个类别的个体数量和其他统计量
#比如得到的实验读数介于0~100，且这些数据以列表形式存储

frame6=frame.rename(columns={'item':'object'})
#可以将实验数据范围均分，比如四部分，就是四个面元(bin)，第一部分0~25，26~50以此类推，用pandas划分面元之前，首先应该定义一个数组，用来存储面元划分的各数值
bins=[0,25,50,75,100]
results=[1,13,46,78,71,45,90,100,10,66]
#然后对results数组应用cut（）函数，同时传入bins变量作为参数
cat=pd.cut(results,bins)#类别性类型，元素是面元的名称
cat.labels#表示元素所属的面元
pd.value_counts(cat)#每个面元出现的数据
#可以用字符串指定面元的名称，把它赋给cut（）函数的labels选项，然后用该函数创建categorical对象
bin_names=['unlikely','less likely','likely','highly likely']
cat2=pd.cut(results,bins,labels=bin_names)
cat3=pd.cut(results,5)#cut函数会按照传入的整数参数，把数组元素的取值范围划分为相应的几部分，而区间上下限取决于样本的最小值和最大值
#除了cut函数，pandas还有qcut()函数直接把样本分为五个面元，cut()划分的每个面元个体数量不同，具体和数据分布有关，而qcut能够保证每个面元的个体数相同，但每个面元的区间大小不等
quintiles=pd.qcut(results,5)#将数据分为5分，每份数据量相等，但范围大小不等
print(quintiles)
'''
#异常值检测后额过滤
'''
randframe=pd.DataFrame(np.random.randn(1000,3))#也可以用random.rand,其中randn是生成标准正态分布的伪随机数（均值为0，方差为1）
#用describe（）查看每一列的描述性统计量
res1=randframe.describe()
#比如将标准差大3倍的元素视作异常值
res2=randframe.std()
#根据每一列的标准差，any（）函数可对每列应用筛选条件，
res3=randframe[(np.abs(randframe)>(3*randframe.std())).any(1)]
print(res3)
'''
#随机取样,排序numpy.random.permutation()函数，调整Series或dataframe对象各行的顺序
'''
nframe=pd.DataFrame(np.arange(25).reshape(5,5))
#用permutation（）函数创建一个包含0~4（顺序随机）这五个整数的数组，将按照这个数组的顺序为dataframe对象的行进行排序
new_order1=np.array([2,3,1,0,4])
new_order2=np.random.permutation(5)
nframe1=nframe.take(new_order2)
#还可以对dataframe的一部分进行排序操作，生成一个数组，只包含特定索引范围的数据
new_order3=[2,3,4]
nframe2=frame.take(new_order3)
#print(new_order3)
#print(nframe2)

#随机取样：从一批数据当中随机抽取一部分
sample=np.random.randint(0,len(nframe),size=3)
nframe3=nframe.take(sample)
print(sample)
print(nframe3)
'''
#6.6字符串处理
#6.6.1内置的字符串处理方法；将符合字符串分为几部分，分别赋值，split（）函数以参考点为分隔点，对文本进行分割
'''
text='16 Bolton Avenue,Boston'
text1=text.split(',')
#切分后的第一元素以空白字符结尾，所以split（）切分后，用strip（）删除多余的空白字符（包括换行符）
token=[s.strip() for s in text1]#其实没啥不一样
#当元素比较少且固定不变时
address,city=[s.strip() for s in text1]
#文本拼接
a=address+','+city#元素少的时候可以用
#元素多的时候，join()函数
strings=['A+','A','A-','B','BB','C+']
b=';'.join(strings)
c='Boston' in text#查找子串，in是否存在
#字符串查找：index（），find（）
d=text.index('Boston')
e=text.find('Boston')
#字符串在文本中出现的次数用count（）函数就好
f=text.count('a')
#针对字符串的替换或删除字符，都用replace（）实现，若用空字符替换子串，等同于删除
g=text.replace('Avenue','Street')
h=text.replace('Avenue','')#等同于删除
i=text.replace('e','')#替换单个字符
print(i)
'''
#6.6.2正则表达式:单条正则表达式是reges,,re模块用于操作regex对象
import re
'''
#re的模块分为：模式匹配；替换；切分。\s+表示一个或多个空白符，re模块中的re.split()可以 以正则表达式作为分隔符对文本进行切分。
text='This is   an\t odd in \n text'
s1=re.split('\s+',text)
#可用re.compile()函数编译正则白大师，得到一个可以重用的正则表达式对象，从而节省CPU周期
regex=re.compile('\s+')#yong compile()函数创建regex对象后，可以直接调用
s2=regex.split(text)
#findall（）函数可匹配文本中所有符合正则表达式的子串，函数返回一个列表，元素是文本中所有符合正则表达式的子串
text1='This is my address:16 Bolton Avenue,Boston'
s3=re.findall('A\w+',text1)
s4=re.findall('[a,A]\w+',text1)#结果中怎么老出现Boston
#跟findall（）函数相关的是math()和search（）。findall返回一列所有符合模式的子串，而search（）函数仅返回第一处符合模式的子串，是一个特殊类型的对象
s5=re.search('[A,a]\w+',text1)#是一个特殊类型的对象,该对象不包含符合模式的子串，而是子串你在字符串中 的开始和结束位置
s51=s5.start()#子串的开始
s52=s5.end()#子串的结束
s53=text1[s51:s52]#子串的完整
#match（）函数从字符串开头开始匹配；如果第一个字符就不匹配，它不会搜索字符串内部，若没找到任何匹配的子串，就不返回任何对象
s6=re.match('[A,a]\w+',text1)#由于第一个字母不是，所有不会往下搜索，所有返回为空
print(text1[s6.start():s6.end()])
'''
#6.7数据聚合：数据处理的最后一步，转换数据，每一个数组生成一个单一的数值；比如sum(),mean(),count（）都是
#6.7.1数据分类，，pandas 中GroupBy工具，其内部机制是SPLIT-APPLY-COMBINE(分组，用函数处理，合并结束)
'''
分组：给定标准，把series或dataframe分为几个不同的组，应用于行或列（axis=0,1）；用函数处理，为每组数据生成单一的值；最后一步是合并
'''
'''
frame=pd.DataFrame({'color':['white','red','green','red','green'],'object':['pen','pencil','pencil','ashtray','pen'],'price1':[5.56,4.2,1.3,0.56,2.75],'price2':[4.75,4.12,1.6,0.75,3.15]})
#使用color列的组标签，计算price1的均值，可以先获取color列，然后调用groupby函数，用参数指定color列
group=frame['price1'].groupby(frame['color'])#分组,把具有相同颜色的行分到一起。
s1=group.groups#调用groups()可以详细看一下dataframe各行的分组情况
s2=group.mean()#对每组数据进行操作
s3=group.sum()

#6.7.3等级分组
#可以使用多列作为多个键，按照等级关系分组
ggroup=frame['price1'].groupby([frame['color'],frame['object']])
s5=ggroup.groups
s6=ggroup.sum()
#可以一次把所有的分组依据和计算方法都指定好，无需定义任何中间变量
s7=frame[['price1','price2']].groupby(frame['color']).mean()
s8=frame.groupby(frame['color']).mean()#整个dataframe的，也就是两列价格
#6.8组迭代，groupby对象支持迭代，生成一系列由各组名称及其数据部分组成的元组

for name,group1 in frame.groupby(frame['color']):
    print(name)
    print(group.sum())

#6.8.1链式转换：分组操作中得到的类型是series或dataframe，他们保留了索引系统和列名称，因为在计算的任一阶段都可以选一列数据’
s9=frame['price1'].groupby(frame['color']).mean()
s10=frame.groupby(frame['color'])['price1'].mean()
s11=frame.groupby(frame['color']).mean()['price1']
#聚合后列名称可能存在表意不明的情况，所以可以对其加前缀而不是完全替代名称，便于跟踪源数据
means=frame.groupby(frame['color']).mean().add_prefix('mean_')
#6.8.2分组函数,有些适合series对象的也可以用
s12=frame.groupby(frame['color'])['price1'].quantile(0.5)#quantile()分位数
#自定义聚合函数，定义好后，将其作为参数传给agg()函数
def range(series):
    return series.max()-series.min()
s13=frame.groupby(frame['color'])['price1'].agg(range)#对其中某一列应用自定义函数
s14=frame.groupby(frame['color']).agg(range)#对整个dataframe应用agg()函数
'''
#6.9高级数据聚合:transforms()和apply()hanshu ,可以把原dataframe和聚合操作得到的计算结果放在一起
'''
frame=pd.DataFrame({'color':['white','red','greeb','red','green'],'price1':[5.56,4.2,1.3,0.56,2.75],'price2':[4.75,4.12,1.6,0.75,3.15]})
sums=frame.groupby(frame['color']).sum().add_prefix('tot_')
frame1=pd.merge(frame,sums,left_on='color',right_index=True)#这里不懂。添加到dataframe对象的每一行
#transform()更适合用于聚合操作，还可以根据每一行的关键字显示聚合结果，对参数有要求：作为参数的函数必须生成一个标量（聚合）

s1=frame.groupby(frame['color']).transform(np.sum).add_prefix('tox_')
#apply():把对象分为几部分后，再用函数处理每一部分，各步骤之间用链式方法接在一起
frame2=pd.DataFrame({'color':['white','black','white','white','black','black'],'status':['up','up','down','down','down','up'],'value1':[12.33,14.55,22.34,27.84,23.4,18.33],'value2':[11.23,31.8,29.99,31.18,18.25,56]})
s1=frame2.groupby([frame2['color'],frame2['status']]).apply(lambda x: x.max())
temp=pd.date_range('1/1/2015',periods=10,freq='H')#periods是指定几点之前
timeseries=pd.Series(np.random.rand(10),index=temp)
timetable=pd.DataFrame({'data':temp,'value1':np.random.rand(10),'value2':np.random.rand(10)})
timetable['cat']=['up','down','left','left','up','up','down','right','right','up']#添加文本值当做基准列
print(timetable)
''' 


print(1)
