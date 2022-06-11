import sympy  as sp
import numpy as np

def f(funcion,x):
    exp=sp.symbols('x')
    evaluar=sp.sympify(funcion).subs(exp,x)
    return(evaluar)

def algoritmo(izq, dere,a):

    ## definimos una variable text que sera una cadena de texto vacia ##
    text= ""
    if izq <= dere :
        text = 'convexa'
        a.append((text))
    if izq >= dere:
        text = 'concava'
        a.append((text))
    return a


funcion=input('Ingrese la funcion a evaluar: ')
x_a=float(input('Ingrese un valor para Xa: '))
x_b=float(input('Ingrese un valor para Xb: '))
dt_l=float(input('Ingrese un valor para \u0394\u03BB: '))

bandera=True
convexa=0
concava=0

dl=np.arange(dt_l,1,dt_l)
a=[]

if dt_l >=0 and dt_l<=1:
    for i in range(len(dl)):
        iz=f(funcion,dl[i]*x_a+(1-dl[i])*x_b)
        de=dl[i]*f(funcion,x_a)+(1-dl[i])*f(funcion,x_b)
        algoritmo(iz,de,a)


for i in range(len(a)):
    if a[i]=='convexa':
        convexa+=1
    if(a[i]=='concava'):
        concava+=1


if concava ==len(a):
    print('la funcion: ',funcion, 'es Concava')
elif convexa==len(a):
    print('la funcion: ',funcion, 'es Convexa')
else:
    print('No aplica para Convexa ni para Concava')