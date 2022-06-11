import numpy as np


def f(x1,x2,teta):
    A=1.20*x1
    B=1.16*x2
    C=teta*(2*pow(x1,2)+pow(x2,2)+(pow(x1+x2,2)))
    exp=A+B-C
    return exp


teta=float(input('Ingrese el valor para \u0398: '))
dx=float(input('Ingrse el valor para \u0394x:'))



x1=0.0
x2=0.0



x1=np.arange(0,5,dx)
x2=np.arange(0,5,dx)
a=[]
b=[]

for x in range(len(x1)):
    for y in range(len(x2)):
        if x1[x]+x2[y]<=5:
            a.append((x1[x],x2[y],f(x1[x],x2[y],teta)))

                

mayor=a[0][2]

for i in range(len(a)):
    if mayor<a[i][2]:
        mayor=a[i][2]
        x_1=a[i][0]
        x_2=a[i][1]

print('f(',x_1,',',x_2,')=',mayor)
