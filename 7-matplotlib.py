# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:52:03 2017

@author: xu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab 

'''
matplotlib不仅可以处理图形，还可以提供事件处理工具，为图形添加动画效果，所以，可以生成以键盘或鼠标移动触发的时间的就好图表
逻辑上，matplotlib整体架构由位于三个不同层级的三层组成，各层之间单向通信，每一层只能与它的下一层通信，而下层无法与商城通信
Scripting(脚本层)；Artist(表现层)；Backend(后端层)
'''
'''
Backend(后端层)是最下面一层，matplotlib API位于该层，这些API事用来在底层实现图形元素的一个个类：FigureCanvas对象实现了绘图区域这一概念
 Renderer对象在FigureCanvas上绘图；Event对象处理用户输入（键盘和鼠标事件）
'''
'''
Artist(表现层)是中间层，图形中所有能看到的元素都是该对象，即标题，轴标签，刻度等组成图形的所有元素是都其实例
 分为两种：原始（primitive）和复合。绘制line2D或矩形等时，形成图形表示的基础元素有primitiva artist 单个对象组成
 多个基础元素组成的图表中的图像元素叫作compsote artist,例如Axis(单条轴)、Ticks(刻度)、Axes(轴)和Figure(图形)，
 Figure对象在Artist的最上面，对应整个图形表示，通常可包括多条轴（Axes）
 Axes对象通常表示图形或图表是对什么内容进行作图的，每个Axes对象只属于一个Figure对象，由两个（三维有三个）Artist Axis 对象组成，标题，x标签和y标签等对象都属于Axes这个compsite artist类型的对象
 Axis对象负责展示在Axes对象上面的数值，定义数值范围，管理刻度（轴上的标记）和刻度值标签（代表每个刻度大小的文本标签），刻度的位置用Locator对象调整，刻度
 标签的格式用Formatter对象调整
'''
'''
Scripting层（Pyplot）:
    pylab模块跟matplotlib一起安装，而pyplot是matplotlib的内部模块，两者导入的方法不同，可选择其中一种进行导入
    pyplot有着自己的命名空间，需要单独导入numpy库，以下使用pyplot模块，它是由一组命令式函数组成，还具有状态性特性，能跟踪当前图形和绘制区域的状态，调用时，函数只对当前图形起作用
'''
#pyplot7.5.1生成一副简单的交互式图表，首先导入matplotlib。pyplot模块，导入时该模块已经实例化可使用，所以把数据给plot()函数，直接使用
'''
plt.plot([1,2,3,4])
plt.show()#其实无需调用show（）也可以直接显示图形
'''
'''
入股只是将一个数字列表或数组传给plt.plot()哈数，matplotlib会嘉定所传入的是突变的Y值，于是将其跟一个序列的x值对应起来，x的取值是0,1,2,3
通常，图形表示的是一对对的（x，y）,因此若想正确定义图表，必须定义两个数组，其中一个数组为x轴的各个值，第二个数组为y轴的值。plot（）还可以接受第三个参数，描述的是数据点在图表中的显示方式
'''
#7.5.2设置图形的属性：默认是：周长与输入数据范围一致；无标题和轴标签；无图例；用蓝色线条连接各数据点
#修改图形，用红点来表示每一对（x,y）,生成一副像模像样的图形
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro')#'ro'是图形显示方式，为点，‘ro-’表示折线连接,'g-'不显示点的折线连接
'''
#可以用列表[xmin,xmax,ymin,yman]定义好x轴和y轴的取值范围，把该列表作为参数传给axis()函数
'''
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.plot([1,2,3,4],[1,4,9,16])
'''
#7.5.3 matplotlib和numpy
#可直接把numpy数组作为输入数据，数组经过pandas处理后，无需做进一步处理，可直接共matplotlib使用
#在同一图形中绘制三种不同的趋势图，使用不同的点形状和线颜色
import math
'''
t=np.arange(0,2.5,0.1)

def f(x):
    return x*x
y1=list(map(math.sin,math.pi*t))#map(函数，列表数据)，得到的是一个列表数据
y2=list(map(math.sin,math.pi*t+math.pi/2))
y3=list(map(math.sin,math.pi*t-math.pi/2))
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')#这个三个都是把连续的变成不连续的点连接：'b*'就是把点变成小星星来显示,'g^'是把点变成深绿色三角形，,'ys'把线变成浅绿色的正方形，
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')#用了不同颜色的线连接了以上面的点
#print(t)
'''
#7.6使用kwargs，子图 subplot(211)三个参数的意思
#组成图表的各个对象由很多用以描述他们特点的属性。他们都有默认值，但可以用关键字（keyword args）设置
'''
plt.plot([1,2,4,2,1,0,1,2,1,4],linewidth=2.0)#linewidth属性可以改变线条的粗细，在plot中直接设置
'''
'''
处理多个Figure和Axes对象;可以同时管理多个图形，而在每个图形中，又可以绘制几个不同的子图，
所以要注意当前Figure和Axes对象的概念（就是Figure中当前所显示的图形）
一副图形中有两个子图的例子，subplot()函数不仅可以将图形分为不同的绘图区域，还能激活特定的子图，以便用命令控制它
subplot()函数用参数设置分区模式和当前子图。只有当前组图会受到命令的影响，subplot（）的参数由三个整数组成：
第一个数字决定图形沿垂直方向被分为几部分，第二个数字决定图形沿着水平方向被分为几部分，第三个数字设定可以直接用命令控制的子图
'''
#绘制两种正弦趋势图（正弦和余弦）。最佳方式是把画布分为上下两个向水平方向延伸的子图。因此，作为参数传入的两个数字分别为211和212
'''
t=np.arange(0,5,0.1)
y1=np.sin(2*np.pi*t)#这里是的在0到5的范围内可以显示多个频率 
y2=np.sin(2*np.pi*t)
plt.subplot(211)#先指定分区模式，2表示垂直方向分为两部分，1表示水平方向是一部分，1表示直接控制的子图是1
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')#也可以变成水平方向的分区
'''
#7.7为图表添加更多元素（文字标签，图例）：有时候会用线条或符号表示数据，用两条轴指定数值范围。
#7.7.1 标题用title（）函数即可，此外还有轴标签，xlabel()和ylabel()函数专门用于添加轴标签，把显示的文本字符串形式传给这两个函数作为参数
'''
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Conting')
plt.ylabel('Square value')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
'''
#可以用关键之参数修改文本属性，比如标题中的字体，轴标签的颜色为灰色，从而反衬图形的标题
'''
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Time New Roman')
plt.xlabel('Conting',color='gray')
plt.ylabel('Square value',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
'''
#还可以在任意位置添加文本，用text（）来实现：text(x,y,s,fontdict=None,**kwargs)
'''
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Time New Roman')
plt.xlabel('Conting',color='gray')
plt.ylabel('Square value',color='gray')
plt.text(1,1.5,'First')#纵坐标多了0.5,因为数字比点要高一点，才不会重叠，每个数据点都有自己的名字
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
'''
#matplotlib 整合了LaTeX表达式
'''支持在图表中插入数学表达式，将表达式内容置于两个$符号之间，可在文本中添加LaTeX
解释器会将该符号之间的文本识别成LaTeX表达式，把他们转换成数学表达式、公式、数学符号或希腊字母等，然后在图像中显示，
通常需要在包含LaTeX表达式的字符串前添加r字符，表明它后面是原始文本，不能对其转义
'''
#可使用关键字参数进一步丰富图形中的文本，比如添加描述图形个数据点趋势的公式，并为公式添加一个彩色边框
'''
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='grey')
plt.ylabel('Square value',color='grey')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(2,15,r'$y=x^2$',fontsize=20,bbox={'facecolor':'red','alpha':0.2})#'facecolor'指的是公式框里的颜色，'alpha指的是颜色的深度是多少
plt.plot([1,2,3,4],[1,4,9,16],'ro')
'''
#7.7.2添加网格
'''
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='grey')
plt.ylabel('Square value',color='grey')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(2,15,r'$y=x^2$',fontsize=20,bbox={'facecolor':'red','alpha':0.2})#'facecolor'指的是公式框里的颜色，'alpha指的是颜色的深度是多少
plt.grid(True)#加网格
plt.plot([1,2,3,4],[1,4,9,16],'ro')
'''
#添加图例：legend（）函数，将图例和字符串类型的图里添加到突变中，以下把四个输入的四个数据点统称为‘First series’
'''
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='grey')
plt.ylabel('Square value',color='grey')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(2,15,r'$y=x^2$',fontsize=20,bbox={'facecolor':'red','alpha':0.2})#'facecolor'指的是公式框里的颜色，'alpha指的是颜色的深度是多少
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro',[1,2,3,4],[1,2,3,4],'b-')
#图例位置默认是1，也就是右上角
#plt.legend(['First series','second'])#图例应该加到plt.plot 后面，不然会娴熟不出来的

#图例默认是添加到右上角，若修改其位置，那么需要添加关键字参数。有loc关键字控制，取值范围是0~10，每个数字代表图中的一处位置，默认为1
plt.legend(['First series','second'],loc=2)#改为右上角
plt.savefig('my_chart.png')#执行这一句代码，工作目录中会生成一个新文件my_chart.png该图像文件的内容就是图标
'''
#7.9处理日期值：在轴上（x）显示日期，问题很多，尤其是用日期做标签事难以管理，日期显示会有问题
#比如图标中有8个数据数据点，按照日-月-年格式再x轴上显示日期值
'''
import datetime
events=[datetime.date(2015,1,23),datetime.date(2015,1,28),datetime.date(2015,2,3),datetime.date(2015,2,21),datetime.date(2015,3,15),datetime.date(2015,3,24),
        datetime.date(2015,4,8),datetime.date(2015,4,24)]
readings=[12,22,25,20,18,15,17,14]
plt.plot(events,readings)
'''
'''
上述时间管理上面，x轴的日期显示方式重叠不清，应定义合适的时间尺度来管理日期，首先导入matplotlib.dates模块，可用于管理日期类型的数据，然后定义时间尺度
这里可以用MonthLocator()和DayLocator()函数，分别表示月份和日子，对于日期格式，只显示必要的刻度标签就好，比如年月，这种格式作为参数传给DateFormatter()函数
定义好两个时间尺度，一个用于日期，一个用于月份，可以在xaxis对象上调用set_major_locator()函数和set_minor_locator函数，为x轴设置两种不同的标签。
此外，月份刻度标签的设置，需要用到set_major_formatter()函数
'''
'''
import matplotlib.dates as mdates#munpy,datetime plt
months=matplotlib.dates.MonthLocator()#用这个函数表示日期，日子
days=mdates.DayLocator()
timeFmt=mdates.DateFormatter('%Y-%m')#这里只显示年月，把这种格式作为参数传给DateFormatter,这里大小写要注意；若显示年月日，那么参数是%Y-%m-%d
events=[datetime.date(2015,1,23),datetime.date(2015,1,28),datetime.date(2015,2,3),datetime.date(2015,2,21),datetime.date(2015,3,15),datetime.date(2015,3,24),
        datetime.date(2015,4,8),datetime.date(2015,4,24)]
readings=[12,22,25,20,18,15,17,14]
fig,ax=plt.subplots()#没有这句，x轴显示的日期会发生变化，而且x轴显示的尺度也不一样
plt.plot(events,readings)
ax.xaxis.set_major_locator(months)#设置主要刻度时间间隔
ax.xaxis.set_major_formatter(timeFmt)#设置时间显示格式
ax.xaxis.set_minor_locator(days)#设置次要刻度时间
'''
#7.10,图标类型，线性图，条状图和饼状图，还有集中复杂却常用的图标
#7.11线性图
'''
线性图最简单，一对对（x,y)值组成的数据点在图表中的位置取决于两条轴（x，y）的刻度范围，比如y=sin(3*x)/x
若要绘制一系列数据点，需要创建两个numpy数组。首先，创建包含x值得数组，用作x轴
'''
#原始y=sin(3*x)/x
'''
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(3*x)/x
plt.plot(x,y)
'''
#扩展，y=sin(n*x)/x,linestyle可以指定线性，linewidth指定宽度
'''
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(x)/x
plt.text(-5,2,r'$y=sin(3*x)/x$')
plt.text(-5,2.25,r'$y=sin(2*x)/x$')
plt.text(-5,2.5,r'$y=sin(x)/x$')
plt.plot(x,y,'k--',linewidth=3)
plt.plot(x,y2,'m--')
plt.plot(x,y3,linestyle='--')
plt.legend(['y','y2','y3'])
'''
#x轴的数值范围是-2*np.pi,但是刻度标签默认使用的是数值形式。需要用pi的倍数，也可以替换y轴刻度的标签
#xticks(),yticks()函数，分别为每个函数传入两列数值。第一个裂变存储刻度的位置，第二个列表存储刻度的标签。
#该例子中的pi显示要用LaTeX
'''
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(x)/x
plt.text(-5,2,r'$y=sin(3*x)/x$')
plt.text(-5,2.25,r'$y=sin(2*x)/x$')
plt.text(-5,2.5,r'$y=sin(x)/x$')
plt.plot(x,y,'k--',linewidth=1)
plt.plot(x,y2,'m--')
plt.plot(x,y3,linestyle='--')
plt.legend(['y','y2','y3'])
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])#只显示这几个数字
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])#只显示整数
'''
#以上x轴和y轴总是置于figure的边缘（跟凸显的边框重合），另一种显示轴的方法是两天轴穿过原点（0，0），也就是笛卡尔坐标轴
'''方法：首先用gca()函数获取Axes对象，通过这个对象，指定每条边的位置：右、左、下、和上，可选择组成图形边框的每条边
使用set_color()函数，把颜色设置为none。删除跟坐标轴不符合的边（右和上）。然后用set_position()函数移动跟x轴和y轴相符的边框，
使其穿过原点（0,0）
'''
'''
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(x)/x
plt.text(-5,2,r'$y=sin(3*x)/x$')
plt.text(-5,2.25,r'$y=sin(2*x)/x$')
plt.text(-5,2.5,r'$y=sin(x)/x$')
plt.plot(x,y,'k--',linewidth=1)
plt.plot(x,y2,'m--')
plt.plot(x,y3,linestyle='--')
plt.legend(['y','y2','y3'])
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])#只显示这几个数字
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])#只显示整数
ax=plt.gca()#获取Axes对象，Axes是子图的含义
ax.spines['right'].set_color('none')#将右边的框的颜色设置成无
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#把x置于bottom上，然后把bottom置于data=0上
ax.spines['bottom'].set_position(('data',0))#set_position:里面的参数是 (position type, amount)’data‘表示把轴放在数据坐标上，这里数据坐标是0
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
'''
#此时，两条轴在图表中部位置交叉，也就是笛卡尔坐标系的原点
'''
用注释和箭头表明曲线上某一数据点的位置，比如可以用LaTeX表达式作为注释，比如添加表示x趋于0时函数sinx/x的极限的公式
matplotlib库的annotate()函数适合用于注释。有多个参数。第一参数为含有LaTeX表达式、要在图形中显示的字符串；随后是各种
各种关键字参数。注释在图表中的位置用存放数据点【x,y】坐标的列表来表示，需把他们传给xy关键字参数。文本注释跟它所揭示的数据点之间
的距离用xytext关键字来指定，用曲线箭头将其表示出来。箭头的属性则由arrowprops关键字参数指定
'''
#annotate()
'''
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(x)/x
plt.text(-5,2,r'$y=sin(3*x)/x$')
plt.text(-5,2.25,r'$y=sin(2*x)/x$')
plt.text(-5,2.5,r'$y=sin(x)/x$')
plt.plot(x,y,'k--',linewidth=1)
plt.plot(x,y2,'m--')
plt.plot(x,y3,linestyle='--')
plt.legend(['y','y2','y3'])
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])#只显示这几个数字
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])#只显示整数
#加上一个有箭头和公式的注释
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}=1$',xy=[0,1],xycoords='data',xytext=[30,30],fontsize=16,textcoords='offset points',
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
ax=plt.gca()#获取Axes对象，Axes是子图的含义
ax.spines['right'].set_color('none')#将右边的框的颜色设置成无
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#把x置于bottom上，然后把bottom置于data=0上
ax.spines['bottom'].set_position(('data',0))#set_position:里面的参数是 (position type, amount)’data‘表示把轴放在数据坐标上，这里数据坐标是0
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
'''
#为pandas数据结构绘制线形图：将dataframe数据结构绘制线性图表，只需把dataframe作为参数传入plot()函数，就能得到多序列线形图
'''
data={'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]}
df=pd.DataFrame({'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]})
x=np.arange(5)
plt.axis([0,5,0,7])
plt.plot(x,df)
plt.legend(data,loc=2)#loc值得是位置
'''
#7.12直方图：每个小矩阵线段连个端点所标识的数据范围也叫面元
'''
pyplot用hist()还绘制直方图，除了绘制外，还以元祖形式返回直方图的计算结果：它能接受一系列样本个体和期望的面元数量作为参数，会把样本范围分成多个区间（面元），
然后计算每个面元所包含的赝本个体的数量，原酸结果可以图形和元组形式返回
'''
#(n,bins,patches),先生成100个0~100的随机数作为样本
'''
pop=np.random.randint(0,100,100)#ranint 的前两个参数是随机取值的范围，第三个是取值数量，randint是整数随机，得到的是np.array([])
#把刚生成的样本数据作为参数传给hist()函数，创建一个直方图，例如：把样本个体分到20个面元中，（默认是分为10个面元），关键字参数bin=20t
n,bins,patches=plt.hist(pop,bins=20)
print(patches)
'''
#7.13条状图，与直方图不同的是x轴表示的不是数值而是类别，用matplotlib中的bar()函数生成
'''
index=[0,1,2,3,4]#这些点处于条状的中心
values=[5,7,2,4,6]
plt.bar(index,values)
'''
#由于每个长条对应的是一种类别，最好用刻度标签标明其类别，方法是把表示各个类别的字符串传递给xticks()参数
#至于刻度标签的位置，需把表示他们在x轴上位置的数值列表传递给xticks()函数，作为第一个参数
'''
index=np.arange(5)
values=[5,7,2,4,6]
plt.bar(index,values)
plt.xticks(index,['A','B','C','D','E'])#这里由于条形在数值中间，所以不需要移动数值，否则可以用index+0.4来代替index
'''
#还可以通过在bar()函数中添加特定的关键字参数来实现，比如，
#把包含标准差的列表传给yerr关键字参数，就能添加标准差，这个参数常跟error_kw参数一起使用，
#而后者又接收其他可用于显示误差线的关键字参数，常用的俩个是eColor和capsize,eColor指定误差线的颜色，
#而capsize指定误差线两头横线的宽度
#还有一个参数alpha，控制彩色条状图的透明度，取值范围是0~1
#在图标中添加图例，用label关键字参数，为图标中的序列指定名称
'''
index=np.arange(5)
values=[5,7,2,4,6]
plt.title('First Bar')#条形图的名称为英文
std1=[0.8,1,0.4,0.9,1.3]#标准差列表
plt.bar(index,values,yerr=std1,error_kw={'eColor':'0.2','capsize':6},alpha=0.9,label='First')
#label='First'表示图例中显示的名称，与添加到legend中一样
plt.xticks(index,['A','B','C','D','E'])
plt.legend(loc=2)
'''
#7.13.1水平条状图，用barh()函数实现，bar（）函数的参数和关键字对该函数依然有效，水平的类别分布在Y轴上，数值显示在x轴
'''
index=np.arange(5)
values=[5,7,2,4,6]
plt.title('A Horizontal Bar Chart')#条形图的名称为英文
std1=[0.8,1,0.4,0.9,1.3]#标准差列表
plt.barh(index,values,xerr=std1,error_kw={'eColor':'0.2','capsize':6},alpha=0.9,label='First')
#label='First'表示图例中显示的名称，与添加到legend中一样
plt.yticks(index,['A','B','C','D','E'])
plt.legend(loc=5)
'''
#相对于垂直的，只需改动几部分，plt.barth.xerr,plt.yticks
#7.13.2多序列条状图，多个长条共用相同的类别，所以可以把每个类别占据的空间分为多个部分，
#想显示几条，就将其分为几个部分（1），可以再增加一个额外的空间，以便区分两个相邻的类别
'''
index=np.arange(5)
values1=[5,7,3,4,6]
values2=[6,6,4,5,7]
values3=[5,6,5,4,6]
bw=0.3
plt.title('A Multiseries Bar Chart')
plt.axis([0,5,0,8])
plt.bar(index,values1,bw)
plt.bar(index+bw,values2,bw)
plt.bar(index+2*bw,values3,bw)
#plt.xticks([0.3,1.3,2.3,3.3,4.3],['A','B','C','D','E'])
plt.xticks(index+bw,['A','B','C','D','E'])#index是数组，所以都加上一个数，还是数组
plt.legend(['values1','values2','values3'],loc=2)
'''
#水平多序列条状图
'''
index=np.arange(5)
values1=[5,7,3,4,6]
values2=[6,6,4,5,7]
values3=[5,6,5,4,6]
bw=0.3
plt.title('A Multiseries Bar Chart')
plt.axis([0,8,0,5])#这里用的方法函数是一样的，里面的参数也是先X后Y，所以数值必须替换
plt.barh(index,values1,bw,color='blue')#水平用barth,color指定颜色
plt.barh(index+bw,values2,bw,color='green')
plt.barh(index+2*bw,values3,bw,color='red')
#plt.xticks([0.3,1.3,2.3,3.3,4.3],['A','B','C','D','E'])
plt.yticks(index+bw,['A','B','C','D','E'])#index是数组，所以都加上一个数，还是数组
plt.legend(['values1','values2','values3'],loc=5)
'''
#7.13.3为pandas dataframe生成多序列条状图
'''
df=pd.DataFrame({'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]})
#n1=df['series1']#取出一组numpy数值
plt.axis([0,5,0,6])
df.plot(kind='barh')#这个好强大，一个就搞定，返回查看311列，dataframe的折线图
plt.yticks(index,['A','B','C','D','E'])
plt.title('Dataframe Bar')#这个要加到后面才有用
#如果需要改动，可以从dataframe中抽取几部分数据，将其保存成numpy组，一个个进行绘图
#制作水平时,改动kind的类型为barh,然后yticks即可
'''
#7.13.4多序列堆积条状图
#表示总和是由几个条状图相加得到的，需要在每个bar()函数中添加bottom关键字参数，把每个序列赋给bottom关键字参数
'''
df=pd.DataFrame({'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]})
series1=df['series1']
series2=df['series2']
series3=df['series3']
plt.axis=[0,5,0,15]
index=np.arange(5)
plt.bar(index,series1,hatch='xx')
plt.bar(index,series2,bottom=series1,hatch='///')#这里的bottom要注意  
plt.bar(index,series3,hatch='\\\\',bottom=(series2+series1))#不少于三个\\\
plt.xticks()
#其实也可以加显示出来数字
#for x,y in zip(index,series1):
 #   plt.text(x,y+0.05,'%d' % y,ha='center',va='bottom')
 '''
#同样水平堆积依然是改动那些指标就可以了，横着的用barth
#7.13.5为pandas dataframe绘制堆积条状图，只需把stacked关键字参数置为True
'''
df=pd.DataFrame({'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]})
df.plot(kind='bar',stacked=True)#相比较于将dataframe做成bar，只是多了一个stacked参数
'''
#7.13.6其他条状图
'''
还有一种图形表示法是条状图表现对比关系，两列有着共同类别的数据，其条状图形分列于x轴两侧，眼Y轴方向
生成。这类图形，需要事先对其中一个序列的y值进行取相反数操作，facecolor 和edgecolor设置不同的颜色即可
如何在长条的末端显示y值标签，for循环，循环体内借助text()函数显示y值标签，标签位置可由ha和va关键字参数来调整
他们分别控制着标签在水平和垂直方向上的对齐效果
'''
'''
x0=np.arange(8)
y1=np.array([1,3,4,6,4,3,2,1])
y2=np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)
plt.bar(x0,y1,0.9,facecolor='b',edgecolor='w')#0.9表示矩形宽度，facecolor 表示矩形的内部填充颜色，edgecolor 表示矩形边缘线条的颜色
plt.bar(x0,-y2,0.9,facecolor='r',edgecolor='w')#句型边缘处为白色比较好
for x,y in zip(x0,y1):#zip(x0,y1)中存储的是一对对（x0,y1）数值
    plt.text(x,y+0.05,'%d' %y,ha='center',va='bottom')
for x,y in zip(x0,y2):
    plt.text(x,-y-1,'%d' % y,ha='center',va='bottom')
 '''
#7.14饼图：用pie()函数制作
'''
该函数仍然要以表示的一列数据作为主要参数。这里直接选用百分比（综合100），实际上可以选用每种类别的实际数值，而让
pie()函数自己去计算每个类别所占的比例。
仍需用关键字设置关键特征，例如：定义颜色列表，为作为输入的数据序列分配颜色，可使用colors关键字参数，把颜色列表
赋值给它；为饼图的每一小块添加标签，使用labels关键字参数，把标签列表赋值给它
此外，为了标准，还需要在代码最后调用axis()函数，用字符串‘equal’作为参数
'''
'''
labels=['Nokia','Samsung','Apple','Lumia']
colors=['yellow','green','red','blue']
values=[10,30,45,15]
plt.pie(values,labels=labels,colors=colors)
#plt.axis('equal')
'''
#制作从圆饼中抽取出一块的效果、阴影，百分比加上去。当我们关注某以块时，会这么用，加入突出Nokia,则使用explode关键字参数，其数据类型是浮点型，取值范围是0~1
#1表示这一块完全脱离饼图；0表示没有抽取，其他表示未完全脱离
'''
labels=['Nokia','Samsung','Apple','Lumia']
colors=['yellow','green','red','blue']
values=[10,30,45,15]
explode=[0.3,0,0,0]
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)#startangle=180表示旋转180度，多了一个参数
#plt.axis('equal')
#还可以在每一块的中间位置添加文本标签来显示百分比(autopct显示百分比，1.1f表示浮点数后面一位，0.2f表示后面两位
#%1.1f%%后面的两个%表示百分比的符号)，用shadow关键字参数添加阴影效果，将其置为True
'''
#为dataframe 制作饼图：每幅饼图只能表示一个序列，使用plot()的kind关键字参数指定图表类型是pie，标准的原型饼图，需添加figsize关键字参数
'''
df=pd.DataFrame({'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]})
df['series1'].plot(kind='pie',figsize=(6,6),autopct='%0.1f%%',shadow=True)
'''
#7.15高级图表：其他图表
#7.15.1 等值线图:由一圈圈封闭的曲线组成的等值线图表示三维结构的表面，用z=f(x,y)生成三维结构，定义x，y的取值范围，确定显示区域，之后用f(x,y)计算每一对（x,y）的值
#得到一个z值矩阵，最后，用contour()函数生成三维结构表面的等值线图，定义颜色表，即用渐变色填充，用逐渐加深的阴影表示负值，数值变大，颜色也变化
'''
dx=0.01
dy=0.01
x=np.arange(-2.0,2.0,dx)
y=np.arange(-2.0,2.0,dy)
X,Y=np.meshgrid(x,y)#函数用两个坐标轴上的点在平面上画格。
def f(x,y):
    return (1-y**5+x**5)*np.exp(-x**2-y**2)#**是几次方，y**5表示y的5次方
C=plt.contour(X,Y,f(X,Y),8,colors='black')#8是清晰度，color是等值线的颜色
plt.contourf(X,Y,f(X,Y),8)
plt.clabel(C,inline=1,fontsize=10)
'''
#在图的一侧增加图例作为对图表中所用颜色的说明，增加colorbar（）函数可实现，黑到红到黄岛白，cmap参数值为plt.cm.hot
'''
dx=0.01
dy=0.01
x=np.arange(-2.0,2.0,dx)
y=np.arange(-2.0,2.0,dy)
X,Y=np.meshgrid(x,y)#函数用两个坐标轴上的点在平面上画格。
def f(x,y):
    return (1-y**5+x**5)*np.exp(-x**2-y**2)#**是几次方，y**5表示y的5次方
C=plt.contour(X,Y,f(X,Y),8,colors='black')#8是清晰度，color是等值线的颜色
plt.contourf(X,Y,f(X,Y),8,cmap=plt.cm.hot)#绘制等值线
plt.clabel(C,inline=1,fontsize=10)
plt.colorbar()#该行可增加图例
'''
#7.15.极区图
'''
若用极区图表示两个不同的数值，分别指定他们在极区图中所占的分量：每块区域的半径r和它所占的角度，其实这就是
极坐标（r,角度），
颜色除了用颜色编码来表示，也可以自定义任意的颜色列表，方法是指定颜色列表，其中每个元素为字符串类型的
RFB编码，格式是#rrggbb,
需要用bar（）函数是，把角度和半径列表传递给它，即可得
'''
'''
N=8
theta=np.arange(0.,2*np.pi,2*np.pi/N)
radii=np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025,0.025,0.95,0.95],polar=True)
#colors=np.array(['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4'])
colors=np.array(['lightgreen','darkred','navy','brown','violet','plum','yellow','darkgreen'])
#两种颜色的表示方法
bars=[plt.bar(theta,radii,width=(2*np.pi/N),bottom=0.0,color=colors)]
'''
#7.16 mplot3d：该工具集是matplotlib内置的标配，可用于实现3D的可视化功能。如果生成的图形在单独的窗口中显示，可用鼠标旋转三维图形的轴进行查看
#mplot3d仍然使用Figure对象，只不过Axes对象要替换为该工具集的Axes3D对象，使用前导入
from mpl_toolkits.mplot3d import Axes3D
'''
#7.16.1 3D曲面 ，使用z=f(x,y)函数；计算出分割线坐标轴，就可以用plot_surface()函数绘制曲面，蓝色三维曲面
fig=plt.figure()
ax=Axes3D(fig)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(X,Y)
def f(x,y):
    return (x**2+y**2)#这里的函数不同，得到的图形不同
    #return (1-y**5+x**5)*np.exp(-x**2-y**2)
ax.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1,cmap=plt.cm.hot)#cmap=plt.cm.hot设置颜色
ax.view_init(elev=30,azim=125)
#修改颜色，比如用cmap参数指定各颜色，也可用view_init()函数旋转曲面，修改elev和azim两个关键字参数，从不同视角查看，
#其中第一个关键字参数指定从哪个高度查看曲面，第二个参数指定屋面旋转的角度，可使用plt.cm.hot颜色表，
'''
#7.16.2 3D散点图：可识别数据点的分布是否遵循某种你特定趋势，是否集聚成簇的趋势
'''
xs=np.random.randint(30,40,100)
ys=np.random.randint(20,300,100)
zs=np.random.randint(10,20,100)
xs2=np.random.randint(50,60,100)
ys2=np.random.randint(30,40,100)
zs2=np.random.randint(50,70,100)
xs3=np.random.randint(10,30,100)
ys3=np.random.randint(40,50,100)
zs3=np.random.randint(40,50,100)
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(xs,ys,zs)
ax.scatter(xs2,ys2,zs2,c='r',marker='^')
ax.scatter(xs3,ys3,zs3,c='g',marker='*')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
'''
#7.16.3 3D条状图，
'''
x=np.arange(8)
y=np.random.randint(0,10,8)
y2=y+np.random.randint(0,3,8)
y3=y2+np.random.randint(0,3,8)
y4=y3+np.random.randint(0,3,8)
y5=y4+np.random.randint(0,3,8)
fig=plt.figure()
ax=Axes3D(fig)
clr=['red','yellow','green','blue','black','brown','violet','navy']
ax.bar(x,y,0,zdir='y',color=clr)
ax.bar(x,y2,10,zdir='y',color=clr)
ax.bar(x,y3,20,zdir='y',color=clr)
ax.bar(x,y4,30,zdir='y',color=clr)
ax.bar(x,y5,40,zdir='y',color=clr)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=40)
'''
#7.17多面板图形：加深表示数据吧一幅图分成多幅子图的情况
#7.17.1在其他子图中显示子图：把图表放入框架，在其他图表中显示，框架就是Axes对象，需要把主Axes对象（主图表）跟防止另一个
#Axes对象实例的框架分开。。用figure()函数渠道Figure对象，用add_axes()函数在它上面定义两个Axes()对象
'''
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])#大图表，
inner_ax=fig.add_axes([0.1,0.1,0.25,0.25])#小图标，左边，下面，右边，上边，四条边,值得是位置
x1=np.arange(10)
y1=np.array([1,2,7,1,5,2,4,2,3,1])#这里轴的范围是可以自动该表的
x2=np.arange(10)
y2=np.array([1,3,4,5,2,6,4,3,1,4])
ax.plot(x1,y1)
inner_ax.plot(x2,y2)
'''
#7.17.12 子图网格:GridSpec()函数可管理更复杂的情况，每幅图各不相同
'''
gs=plt.GridSpec(3,3)
fig=plt.figure(figsize=(6,6))#两个参数分别是宽度和高度
fig.add_subplot(gs[1,:2])#左边上数第二，第一个参数是行，第二是列，：2表示到第2/3的位置
fig.add_subplot(gs[0,:2])#左边上数第一
fig.add_subplot(gs[2,0])#左边上数第三
fig.add_subplot(gs[:2,2])#右边边上数第一，第一个:2是持续到第二行
fig.add_subplot(gs[2,1:])#右边上数第二，1：是1/3之后
'''
#子图的使用方法，在add_subplot()函数（相当于上边的add_axes）返回的Axes对象上调用plot（）函数
'''
gs=plt.GridSpec(3,3)
fig=plt.figure(figsize=(6,6))
x1=np.array([1,3,2,5])
y1=np.array([4,3,7,2])
x2=np.array([0,1,2,3,4])
y2=np.array([3,2,4,6,4])
s1=fig.add_subplot(gs[0,:2])
s1.plot(x1,y1,'r')
s2=fig.add_subplot(gs[1,:2])
s2.bar(x2,y2)
s3=fig.add_subplot(gs[2,0])
s3.barh(x2,y2,color='green')
s4=fig.add_subplot(gs[:2,2])
s4.plot(x2,y2,'k')
s5=fig.add_subplot(gs[2,1:])
s5.plot(x1,y1,'b^',x2,y2,'yo')
'''
'''
a='12'
for i in range(1,11):
    c=a+str(i)
    print(c,type(c))
'''

'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
diabetes=datasets.load_diabetes()
data=diabetes.data
target=diabetes.target
x_train=data[:-20][:,2]
x_test=data[-20:][:,2]
y_train=target[:-20]
y_test=target[-20:]
#x_train=x_train[:,np.newaxis]#x_train是一行，然后x0_train变成一列
#x_test=x_test[:,np.newaxis]
#x_test.sort(axis=0)#axis=0表示升序排列，最小的在最上面，axis=1是降序排列
#x_test=x_test*100#因为原来里面的数字小数，所以*100方便计算
#x_train=x_train*100
print(len(y_test),len(x_test))
plt.axis=[-10,10,0,350]
#plt.scatter(x_test,y_test)
'''