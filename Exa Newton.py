import sympy
from sympy import *
import numpy
from numpy import *
import sys

def evaluar(f,x):
	r = eval(f)
	return r

def matriz_hessiana(f, x_symbol, x):
	derivada1_fx = sympy.diff(f, x_symbol)
	derivada2_fx = sympy.diff(derivada1_fx, x_symbol)

	hess = eval(str(derivada2_fx))

	m_hessiana = Matrix([[hess]])
	return m_hessiana

def gradiente(f, x_symbol, x):
	derivada_fx = sympy.diff(f, x_symbol)
	gradiente = eval(str(derivada_fx))
	return gradiente

def algoritmo(func, x_n1, xn, t, e):
	norm_diferent_x = numpy.linalg.norm(numpy.array(x_n1 - xn, dtype = numpy.float32))
	while(norm_diferent_x >= e):
		norma_xn_mas1 = numpy.linalg.norm(numpy.array(x_n1, dtype = numpy.float32))
		norma_xn = numpy.linalg.norm(numpy.array(xn, dtype = numpy.float32))

		print (norma_xn_mas1, norma_xn)

		if(norma_xn_mas1 < norma_xn):
			g0 = norma_xn
			norm_diferent_gradient = numpy.linalg.norm(numpy.array((gradiente(func, x, x_n1) - gradiente(func, x, xn) ), dtype = numpy.float32))
			g_prim0 = - g0 / norm_diferent_gradient
			g1 = numpy.linalg.norm(numpy.array(gradiente(func, x, x_n1), dtype = numpy.float32))
			t_prim = max([-g_prim0 / 2.0 * (g1 - g0 - g_prim0), 0.1])
			x_n1 = float((1 - t_prim) * xn + t_prim * x_n1)

		xn = x_n1
		norm_diferent_x = numpy.linalg.norm(numpy.array(x_n1 - xn, dtype = numpy.float32))
		return [x_n1 , evaluar(func, x_n1)]

x = sympy.symbols("x")

func = "-5 * x**2 + 3*x - 2"
t = 0.9
e = sys.float_info.epsilon

xn = 0
hessiana = matriz_hessiana(func, x, xn).inv()
x_n1 = xn - t * hessiana[0] * gradiente(func, x, xn)

punto_optimo = algoritmo(func, x_n1, xn, t, e)
print ("Punto optimo: ", punto_optimo)
