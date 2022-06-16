import sympy as sp

def Hessiana(funcion,xa,xb):
    x,y=sp.symbols('x,y')
    parcial_x=sp.diff(funcion,x,2).subs(x,xa).subs(y,xb)
    parcial_y=sp.diff(funcion,y,2).subs(y,xb).subs(x,xa)
    parcial_xy=sp.diff(funcion,x,y).subs(x,xa).subs(y,xb)
    return(parcial_x,parcial_y,parcial_xy)

def Algoritmo(p_x,p_y,p_xy):

    A=p_x*p_y
    B=pow(p_xy,2)
    C=A-B

    if(C<0):
        return 'Punto silla'
    elif(C>0 and p_x<0):
        return 'Maximo Local'
    elif(C>0 and p_x>0):
        return 'Minimo Local'
    elif(C==0):
        return('no existe información suficiente sobre el punto')
    

funcion='-5*y^2+6*y*x+590*y-3*x^2-90*x-28800'
xa=110.0
xb=125.0

p_x=Hessiana(funcion,xa,xb)[0]
p_y=Hessiana(funcion,xa,xb)[1]
p_xy=Hessiana(funcion,xa,xb)[2]

print(Algoritmo(p_x,p_y,p_xy))

