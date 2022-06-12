from matplotlib import pyplot
import sympy


def Primera(exp,v_x):
    ex=sympy.symbols('x')
    deri=sympy.diff(exp,ex)
    expresion=sympy.sympify(deri)
    derivada=expresion.subs(expresion,v_x)
    return derivada

def Segunda(exp,v_x):
    ex=sympy.symbols('x')
    deri=sympy.diff(exp,ex,2)
    expresion=sympy.sympify(deri)
    derivada=expresion.subs(expresion,v_x)
    return derivada

def f1(exp,x):
    fx=sympy.symbols('x')
    valor=sympy.sympify(exp).subs(fx,x)
    return valor

def f2(exp,v_x,dt_x,v_t):
    der=f1(exp,v_x)+(Primera(exp,v_x)*dt_x)+1/2*dt_x*(Segunda(exp,v_x+v_t*dt_x))*dt_x
    return(der)


exp=input('Ingrese la Función a graficar: ')
x_a=int(input('Ingrese los valor superior del rango A: '))
x_b=int(input('Ingrese los valor superior del rango B: '))
t=float(input('Ingrese el valor para t: '))
dt_x=float(input('Ingrese el valor para \u0394x: '))


if(x_b<x_a):
    aux=x_b
    x_b=x_a
    x_a=aux

x = range(x_a, x_b)
# Graficar ambas funciones.
pyplot.plot(x, [f1(exp,i) for i in x ],color="red", label="f(x)")
pyplot.plot(x, [f2(exp,i,dt_x,t) for i in x ],color="blue", label="Teorema de Taylor")
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(x_a, x_b)
pyplot.ylim(x_a, x_b)



# Mostrarlo.
pyplot.legend(loc='upper right')
pyplot.show()