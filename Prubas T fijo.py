from sklearn.metrics import jaccard_score
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
    return y**4+x**4-13*y**2-21*x**2+2*x**2*y-22*y+2*x*y**2-14*x+170

funcion='sin(x+y)+(x-y)^2-1.5*x+2.5*y-1'
t=0.01
n=0.01
gra=(0.0,0.0)
dx=(0.0,0.0)
x_n=0.0
y_n=0.0
xn=3
yn=4
j=[]
h=[]

norma=(Gradiente(funcion,xn,yn)[0]**2+Gradiente(funcion,xn,yn)[1]**2)**1/2
while norma >=n:
    dx=(Gradiente(funcion,xn,yn)[0]*-1,Gradiente(funcion,xn,yn)[1]*-1)
    x_n=xn+t*dx[0]
    y_n=yn+t*dx[1]
    xn=x_n
    yn=y_n
    norma=(Gradiente(funcion,xn,yn)[0]**2+Gradiente(funcion,x_n,y_n)[1]**2)**1/2
    h.append(xn)
    j.append(yn)
    print(xn,yn)

x = np.linspace(2,3 , 100)
y = np.linspace(2,3, 100)
X, Y = np.meshgrid(x, y)
Z = g(X, Y)

fig,ax=plt.subplots()
b=ax.contourf(X,Y,Z)
fig.colorbar(b)

plt.plot(h,j,color='red')

plt.show()