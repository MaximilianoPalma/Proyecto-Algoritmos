import sympy as sp

def algoritmo(funcion,a):
    x,y=sp.symbols('x,y')
    parcial_x= sp.diff(funcion,x)
    parcial_y=sp.diff(funcion,y)
    a.append((parcial_x,parcial_y))
    return a

a=[]

funcion='sin(x+y)+(x-y)^2-1.5*x+2.5*y+1'
print(algoritmo(funcion,a))
