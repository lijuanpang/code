# -*- coding:utf-8 -*-

sum = 0
x = 0
while True:
    x = x + 1
    if x % 2 == 0:
        continue
    sum = sum + x
    if x >= 99:
        break
print(sum)
print("A")

'''
for x in ['A','B','C']:
    for y in ['1','2','3']:
        print(x+y)
'''
'''
#dict查找速度快，内存大，key不能重复，无序
d = {
    'Adam':95,
    'Lisa':85,
    'Bart':59
    }
##print(len(d))
#第一种方法
if 'Adam' in d:
    print(d['Adam'])
#第二种方法
##print(d.get('Adam'))
print('Adam:' + str(d['Adam']))
print('Lisa:' + str(d['Lisa']))
print('Bart:' + str(d['Bart']))
for key in d:
##    print(key)
    print(key+':'+str(d[key]))

'''
'''
##set不重复，无序
s = set(['A','B','C'])
s.remove('A')
print(s)

##print(s)
##if 'B' in s:
##    print(1)
n=set(['A','B','C'])
for x in s:
    n.add(x.lower())
    print(n)
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x[0]+':'+str(x[1]))
 
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print(s)
'''
'''
L=[]
for i in range(1,101):
    L.append(i*i)
print(sum(L))
##另一种方法：L = [x*x for x in range(1,101)]
'''
'''
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-1))
'''
'''
def square_of_sum(x):
    sum = 0
    for i in x:
        sum = sum+i*i
    return sum
print(square_of_sum([1,2]))
'''
'''
import math
def move(x,y,step,angle):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
##r= move(100,100,60,math.pi/6) 也可以返回同样的数字，所以函数返回的仍是但一值。返回tuple
'''
'''
import math
def quadratic_equation(a,b,c):
    A= b*b-4*a*c
    if A>=0:
        x1=(-b+math.sqrt(A))/(2*a)
        x2=(-b-math.sqrt(A))/(2*a)
    else:
        x1=none
        x2=none
    return x1,x2
print(quadratic_equation(2, 3, 0))

def fact(n):
	if n == 1:
		mul=1
	else:
		mul=fact(n-1)*n
	return mul
'''
'''
def move(n,a,b,c):
    if n==1:
        print('A-->C')
    else:
        print('A-->B')
        move(n-1,b,a,c)
        print('A-->C')
        '''
'''
def average(*args):
    n=len(args)
    if n==0:
        return 0
    else:
        sum1=sum(args)
        return (sum1/n)
            
print(average())   
print(average(1, 2))
print(average(1, 2, 2, 3, 4))
'''
'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
r=[]
n=3
for i in range(3):
    r.append(L[i])
print(r)
L1=L[0:1]
L2=[:]#表示复制一个L
L3[::2]#每两个取出一个来,切片时后面的数字表示的取出几个数字而不是列表下标
##tuple进行切片时一样
print(L1)

#1. 前10个数；2. 3的倍数；3. 不大于50的5的倍数。
L = range(1, 101)
print(L[:10])
print(L[2::3])
print(L[4:50:5])
print(L[-2:])#后两个
print(L[:-2])#前两个
print(L[-3:-1])#倒数第三个到倒数第二个

print('ABCDEFG'[1:])
#1. 有序集合：list，tuple，str和unicode；2. 无序集合：set 3. 无序集合并且具有 key-value 对：dict

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index,name in enumerate(L):
    print(index,'-',name)
'''
# 对于dict d,for v in d.values():是依次取出d中的‘value’;d.items()是取出d中的元素
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
t=0
for k ,v in d.items():
    sum = sum+v
    t=t+1
    print(k,':',v)
print('average',':',sum/t)
'''
#[x*x for x in range(1,11)]
#列表生成式的 for 循环后面还可以加上 if 判断
[x*x for x in range(1,11) if x%2==0]
print([m+n for m in 'ABC' for n in '123'])#['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
