import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import random as r

def Gradiente(funcion,x1,x2):
    x,y=sp.symbols('x,y')
    p_x=sp.diff(funcion,x).subs(x,x1).subs(y,x2)
    p_y=sp.diff(funcion,y).subs(x,x1).subs(y,x2)
    return p_x,p_y

def g(x,y):
    return (x+2*y-7)**2+(2*x+y-5)**2

funcion='(x+2*y-7)^2+(2*x+y-5)^2'
#funcion='sin(x+y)+(x-y)^2-1.5*x+2.5*y-1'
t=0.1
n=0.00001
gra=(0.0,0.0)
dx=(0.0,0.0)
x_n=0.0
y_n=0.0
xn=r.randint(-10,10)
yn=r.randint(-10,10)
j=[]
h=[]


norma=(Gradiente(funcion,xn,yn)[0]**2+Gradiente(funcion,xn,yn)[1]**2)**1/2
while norma >=n:
    dx=(Gradiente(funcion,xn,yn)[0]*-1,Gradiente(funcion,xn,yn)[1]*-1)
    x_n=xn+t*dx[0]
    y_n=yn+t*dx[1]
    xn=x_n
    yn=y_n
    norma=(Gradiente(funcion,x_n,y_n)[0]**2+Gradiente(funcion,x_n,y_n)[1]**2)**1/2
    h.append(xn)
    j.append(yn)
    print(xn,yn)

x = np.linspace(-10,20 , 100)
y = np.linspace(-10,20, 100)
X, Y = np.meshgrid(x, y)
Z = g(X, Y)
fig,ax=plt.subplots()
b=ax.contourf(X,Y,Z)
fig.colorbar(b)

xi=h[0]
yi=j[0]
xf=h[-1]
yf=j[-1]


plt.plot(h,j,color='red',marker='o')
plt.plot(xi,yi,marker='o',color='blue',label='Comienzo: ('+str(xi)+','+str(yi)+')')
plt.plot(xf,yf,marker='o',color='green',label='Final: ('+str(xf)+','+str(yf)+')')
plt.legend()
plt.show()

