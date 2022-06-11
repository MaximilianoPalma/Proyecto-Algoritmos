import sympy as sp

def Derivada(funcion,valor):
    x=sp.symbols('x')
    der=sp.diff(funcion,x)
    resultado=sp.sympify(der).subs(x,valor)
    return resultado

def Derivada_Numerica(exp,valor,delta_x):
    x=sp.symbols('x')
    izq= (sp.sympify(exp).subs(x,valor+delta_x))
    der=((sp.sympify(exp).subs(x,valor)))
    derivada=(izq-der)/delta_x
    return derivada

funcion=input('Introduce la función en términos de x: ')
valor=float(input('Ingrese el valor para x: '))
dt_x=float(input('Ingrese el valor para \u0394x: '))
eps=float(input('Ingrese el valor para \u03B5: '))
bandera=True

while bandera:
    derivada=Derivada_Numerica(funcion,valor,dt_x)
    derivada_full= Derivada(funcion,valor)
    full=abs(derivada_full-derivada)
    if full<eps:
        funcion/=2
    else:
        bandera=False
    print('d/d(x)= ',full,',\u03B5= ',eps,',',str(chr(916))+ 'x= ', dt_x )
   

print('El valor de '+str(chr(916))+'x es: ',dt_x)
