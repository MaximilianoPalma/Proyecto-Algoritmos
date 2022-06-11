import sympy as sp

def f(funcion,valor):
    x=sp.symbols('x')
    exp=sp.sympify(funcion).subs(x,valor)
    return exp

funcion=input('Ingrese la función a evaluar: ')
valor=float(input('Ingrese el valor de x:'))
dt_x=float(input('Ingrese el valor para \u0394x: '))

if dt_x>=0 and dt_x<=1:
    izq=f(funcion,valor+dt_x)
    der=f(funcion,valor)
    total=(izq-der)/dt_x

print(total)
