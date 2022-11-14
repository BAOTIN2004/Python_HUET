import random
import numpy as np
from numpy import random 
x1=[]
print('Moi ban nhap lan luot 7 phan tu cua x1:')
for i in range(0,7,1):
    x1.append((int(input())))
print('Bai 1:',x1)
x2=[]
for i in range(0,30,1):
    x2.append(random.randint(-10,10))
print('Bai 2',x2)
x3=[]
for i in range(0,30,1):
    x3.append(random.uniform(-5.7,6.9))
print('Bai 3:',x3)
x4=[]
x5=[]
a=int(input('Nhap a = '))
for i in range(0,10,1):
    x4.append(random.randint(-1000,1000))
    x5.append(x4[i]*a)
print('Bai 4:')
print('Vec to x4:',x4)
print('Ket qua cua phep nhan vecto x4 va',a,'la:',x5)
x6=[]
x7=[]
x8=[]
x9=[]
for i in range(0,15,1):
    x6.append(random.randint(-100,100))
    x7.append(random.randint(-100,100))
    x8.append(x6[i]+x7[i])
    x9.append(x6[i]-x7[i])
print('Bai 5:')
print('Vecto x:',x6,'\nVecto y',x7)
print('Ket qua cua phep cong vec to x va y: x+y =',x8)
print('Ket qua cua phep tru vec to x va y: x-y =',x9)
x10=[]
x11=[]
x12=[]
for i in range(0,10,1):
    x10.append(random.randint(-10,10))
    x11.append(random.randint(-10,10))
    x12.append(x10[i]*x11[i])
print('Bai 6:')
print('Vecto x:',x10,'\nVecto y:',x11,'\nKet qua cua phep nhan elementwise multiplication của 2 vector x va y =',x12)
x13=[]
x14=[]
x15=[]
s=0
for i in range(0,10,1):
    x13.append(random.randint(-10,10))
    x14.append(random.randint(-10,10))
    s+=(x13[i]*x14[i])
print('Bai 7: \nVecto x:',x13,'\nVecto y:',x14,'\nKet qua cua phep tinh tich vo huong 2 vecto x va y =',s)
A=random.randint(0,10,size=(3,5))
print('Bai 8:\n','Ma tran A:\n',A,'\nPhan tu A23:',A[1,2])
b=int(input('Moi ban nhap b:'))
print('Bai9\nKet qua cua phep nhan',b,'va ma tran A:\n',A*b)
B=random.randint(0,10,size=(3,5))
print('Bai 10\nKet qua cua phep cong ma tran A va B:\n',A+B)
C=random.randint(0,10,size=(3,4))
D=random.randint(0,10,size=(4,5))
print('Bai 11:\nMa tran C:\n',C ,'\nMa tran D:\n',D,'\nKet qua cua phep nhan ma tran C va D:\n',C@D)