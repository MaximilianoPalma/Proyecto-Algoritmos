import sympy as sp

def algoritmo(funcion,a):
    x,y=sp.symbols('x,y')
    parcial_x= sp.diff(funcion,x)
    parcial_y=sp.diff(funcion,y)
    a.append((parcial_x,parcial_y))
    return a

a=[]

funcion=input('Ingrese la función a evaluar con dos variables: ')

print(algoritmo(funcion,a))
