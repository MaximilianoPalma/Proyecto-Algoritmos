import sympy as sp
from sympy.matrices import Matrix

x,y = sp.symbols('x,y')
f ='(x^2+y-11)^2+(x+y^2-7)^2'
t = 0.01
eta = 0.000001
inputpunto = input('Ingrese un Punto (x,y) separado unicamente por una coma: ').split(',')
aPunto = Matrix([[inputpunto[0]],[inputpunto[1]]])
grad = Matrix([[sp.diff(f,x)],[sp.diff(f,y)]])
while(float(grad.subs([(x, aPunto[0]), (y, aPunto[1])]).norm()) >= eta):
    delx = -grad.subs([(x, aPunto[0]), (y, aPunto[1])])
    aPunto = aPunto + t*delx
    print(aPunto)

print ('El punto optimo en la funcion ',f,', es: ('+str(aPunto[0])+','+ str(aPunto[1])+ ')')