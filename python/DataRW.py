# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:34:17 2017

@author: xu
"""
import pandas as pd
import numpy as np
import html5lib#安装时用的是condapip install xxx
import lxml 
import xml.dom.minidom
from pandas.io.json import json_normalize
import json
from pandas.io.pytables import HDFStore
import pickle 
#读取函数：read_csv,read_excel,read_hdf,read_sql,read_json,read_html,read_stata,read_clipboard,read_pickle,read_msgpack,read_gbq
#写入函数:to_csv,等，最后两个是带实验性质的，
#列表形式的数据，用逗号的是csv，还有用空格和制表符分隔的列表数据：read_csv，read_table,to_csv
#读取后将其转换为Dataframe文件
'''
csvframe1=pd.read_csv('myCSV_01.csv')#若myCSV_01.csv和DataRW在同一个文件夹，那么可以直接写名称，否则需要加入路径
csvframe2=pd.read_table('myCSV_01.csv',sep=',')#csv可被视为文本文件，故可以用这个函数，但是需要制定分隔符
#对于没有表头的csv文件，需要使用header将其值置为none，pandas将为其添加默认表头
csvframe3=pd.read_csv('myCSV_02.csv',header=None)
#或者使用names指定表头，直接把存有各列名称的数组赋给它即可
csvframe4=pd.read_csv('myCSV_02.csv',names=['white','red','blue','green','animal'])
#读取csv并创建一个有等级结构的dataframe对象，可把所有想转化为索引的列名称赋给index_col
csvframe5=pd.read_csv('myCSV_03.csv')
csvframe6=pd.read_csv('myCSV_03.csv',index_col=['color','status'])                    
print(csvframe6)
'''
#用regexp解析txt文件，使用sep指定正则表达式，在read_table()中使用，\s*通配符，可以兼顾空格或制表符，只有制表符也可以用\t，*表示这些字符可能有多个
#最常用通配符：数字\d；非数字字符\D；空白字符 \s；空白字符  \S；换行符 \n ；制表符\t；用十六进制数字xxx表示的unicode; \uxxx 换行符以外的单个字符.
'''
txt1=pd.read_table('ch05_04.txt',sep='\s*')#生成是dataframe文件
txt2=pd.read_table('ch05_05.txt',sep='\D*',header=None)#当分隔符为字母的时候可以用
#解析数据时把空行排除在外，文件表头或没有必要的注释。使用skiprows，注意：排除前五行用skiprows=5；排除第五行skiprows=[5]
txt3=pd.read_table('ch05_06.txt',sep=',',skiprows=[0,1,3,6])
#print(txt3)
'''
#从txt中读取部分数据：处理大数据或只对文件部分数据感兴趣时，需要按照部分读取文件，需要迭代
#指定起始行n(n=skiprows)和从起始行往后读多少行（nrows=i）
'''
csvframe7=pd.read_csv('myCSV_02.csv',skiprows=[1],nrows=5,header=None)#[2]是第一行？
out=pd.Series()
i=0
pieces=pd.read_csv('myCSV_01.csv',chunksize=3)#一次取三行数值，且每次数值都有表头
#对于列表生成式，可以用循环的方式得出数据

for i in pieces:
    print(i)
    


for piece in pieces:
    out.set_value(i,piece['white'].sum())#如何往空的Series中放元素，下标加元素、
    i=i+1

print(out)
'''
#往csv中写数据 dataframe,list 数据不可以这么用
'''
frame2=pd.DataFrame(np.arange(16).reshape(4,4),index=[0,1,2,3],columns=['ball','pen','pencil','paper'])
frame2.to_csv('ch05_07.csv')#将所有数据写入
frame2.to_csv('ch05_071.csv',index=False,header=False)#索引与列名称不写入，只写入数据
frame3=pd.DataFrame([[1,2],[np.NaN,0]],index=['blue','green'],columns=['ball','mug'])#np.NaN,写入后是空字符
#可以to_csv函数中的na_rep选项把空字段替换为需要的值，常用值有：NULL,0,NaN,字段
frame3.to_csv('ch05_09.csv',na_rep='NaN')
frame3.to_csv('ch05_08.csv')
print(frame3)
#以上函数也适合把series写入
'''
#读写html文件read_html(),to_html(),可将Dataframe转化为html表格，也可以读取网页数据
'''
frame=pd.DataFrame(np.arange(4).reshape(2,2),index=['l','o'],columns=['v','e'])
#print(frame)
#print(frame.to_html())#打印出表格

s= ['<HTML>']
s.append('<HEAD><TITLE>MY DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html=''.join(s)
html_file=open('myFrame.html','w')
html_file.write(html)
html_file.close()
#read_html()解析html页面时，寻找HTML表格，然后将其转化为dataframe
web_frames=pd.read_html('https://kf.07073.com/l')
print(web_frames)
#print(s1[0])#由于这里只有一个元素，因此索引为0
'''
#从网页中的表格爬取数据，然后保存到csv文件中
'''
web=pd.read_html('https://kf.07073.com/')
s0=open('web.csv','w')
s0.write(str(web))#这里一定要是字符串
s0.close()
'''
#从xml读取数据，可以使用lxml库;不太懂
'''
xml=objectify.parse('F:/python3/Book.xml')
print(xml) 
'''
dom=xml.dom.minidom.parse('F:/python3/Book.xml')#用于打开一个xml文件，并将这个文件对象dom变量。
root=dom.documentElement#返回文档的 documentElement:并给root
#每个节点都有它的nodeName,nodeValue,nodeType
'''
print(root.nodeName) #得到根节点名称   
print(root.nodeValue)#节点的值，对文本节点有效
print(root.nodeType)#节点类型catalog是ELEMENT_NODE节点的类型
print(root.ELEMENT_NODE)
print()            
#对于知道元素名字的子元素，可以使用getElementBy TagName方法来获取
bb=root.getElementsByTagName('login')
b=bb[0]
print(b.nodeName)
'''
#读写excel文件，to_excel,read_excel并转成dataframe
'''
excel1=pd.read_excel('data.xlsx')#默认读取第一个工作表的数据
#print(excel1)
excel2=pd.read_excel('data.xlsx','Sheet2')#读取第二个工作表的数据
#print(excel2)
frame=pd.DataFrame(np.random.random((4,4)),index=['exp1','exp2','exp3','exp4'],columns=['Jan2017','Fab2017','Mar2017','Apr2017'])
#np.random.random((4,4))这里是双括号
#print(frame)
frame.to_excel('data2.xlsx')
'''
#JSON数据（）
'''JSON数据（）JavaScript object notation，JavaScript的对象标记，常用标准数据格式之一，在web数据的传输方面
使用read_json(),to_json()函数，检查json格式可用JSONViewer，网址http://jsonviewer.stack.hu/,输入和赋值json到该应用中，
'''
'''
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['white','black','red','blue'],columns=['up','down','right','left'])
frame.to_json('frame.json')
frame0=pd.read_json('frame.json')
print(frame0)
'''
#json文件中的数据通常是列表形式，因为是dataframe转化来的，但对于不是列表形式的json文件，进行规范化,json_normalize()可将字典或列表转为表格
'''
                                                                         data1=[{"writer":"Mark Ross","nationality":"USA","books":[
        {"title":"XML Cookbook","price":23.56},
        {"title":"Python Fundamentals","price":50.70},
        {"title":"The NumPy library","price":12.30}]
    },
    {"writer":"Barbara Bracket","nationality":"UK","books":[
           { "title":"Java Enterprise","price":28.60},
           {"title":"HTML5","price":31.35},
           {"title":"Python for Dummies","price":28.00}
           ]
    }]
file=open('books.json','r')
text=file.read()
text=json.loads(text)
print(json_normalize(text,'books'))#读取以books作为键的元素的值，
json_normalize(text,'books',['writer','nationality'])#将其作为第三个参数传入即可
#其实这个运行是错的，因为books.json出现了问题
'''
#若要分析大量的数据，最好使用二进制格式，HDF5：代表等级数据格式，PyTables 和h5py
#pandas 中还有HDStore,类似于dic的类，用于PyTables对象，但必须先导入HDFStore 类
'''
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['white','black','red','blue'],columns=['up','down','right','left'])
frame2=pd.DataFrame(np.random.rand(4,4),index=['white','black','red','blue'],columns=['up','down','right','left'])
#创建一个mydata.h5的HDF5文件，用于储存数据
store=HDFStore('mydata.h5')#新建一个HDF5文件，保存数据
store['obj1']=#可以把多个数据结构存储到一个HDF5文件中，比如store变量表示的这个文件
store['obj2']=frame2
print(store['obj1'])
'''
#pickle-python对象序列化，可对用Python实现的数据结构进行序列化和反序列化操作，序列化是把对象的层级结构转换为字节流的过程。cPickle模块
'''
#用Pickle模块实现Python对象序列化，默认使用ASCII表达式
#创建具有内部结构的足够复杂的对象，比如字典对象
data={'color':['white','red'],'value':['5','7']}
#接着用cPickle 模块的dumps()函数对data对象执行序列化操作
pickle_data=pickle.dumps(data)
print(pickle_data)
nframe=pickle.loads(pickle_data)#loads()函数能够重建被序列化的对象（反序列化）
print(nframe)
'''
#用pandsa实现对象序列化，不需导入，序列化格式并不是完全使用的ASCII编码,直接生成.pkl文件
frame=pd.DataFrame(np.arange(16).reshape(4,4),index=['white','black','red','blue'],columns=['up','down','right','left'])
frame.to_pickle('frame.pkl')
read_frame=pd.read_pickle('frame.pkl')
#print(read_frame)