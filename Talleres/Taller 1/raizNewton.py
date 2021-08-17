import sympy as sy 
from sympy import *
import math
from math import copysign 
from mpmath import mp, mpf
import matplotlib.pyplot as plt

#implementacion de Metodo de Biseccion
def metodoBiseccion(a,b,e,funcion):

    sign = lambda x : copysign(1, x) # variable que dice si el signo de un valor es negatibo (-1) o si es positivo (1)
    iteraciones = 0
    while mpf(b - a)> e:
        c = mpf((a+b)/2)
        if valorFuncion(funcion,c) == 0: 
            return mpf(c)
        else:
            if sign(valorFuncion(funcion,c)) == sign(valorFuncion(funcion,a)):
                a = mpf(c)
            else:
                b = mpf(c)
        iteraciones += 1
    arregloIteracionesBiseccion.append(iteraciones) 
    print("El numero de iteraciones por Biseccion fue de: " + str(iteraciones))
    return mpf(c) 

# implementacion de metodo de Newton
def metodoNewton(v, e, funcion):
    
    #asignacion inicial del valor de la raiz
    r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    iteraciones = 0
    while abs(mpf(r - v)) > e:
        iteraciones = iteraciones + 1
        #validacion de un numero de iteraciones
        if iteraciones > 1000:
            arregloIteracionesNewton.append(0)
            return 0
        v = r
        #reasignacion de la raiz
        r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    print("El numero de iteraciones por Newton fue de: " + str(iteraciones))
    arregloIteracionesNewton.append(iteraciones)
    return mpf(r)
    
# funcion que evalua el valor de la funcion
def valorFuncion(funcion,v):
    return funcion.evalf(subs = {x:v}) 

# funcion que calcula la derivada de la funcion 
def derivada(funcion, v):
    deriv = sy.diff(funcion,x)
    return deriv.doit().subs({x:v}).evalf()

#main
#definicion de los parametros y funciones necesarias
x = sy.Symbol('x')
funcion1 = (cos(x))**2 - x ** 2
funcion2 = x * sin(x) - 1
funcion3 =  x ** 3 - 2*(x**2) + ((4/3)*x) - 8/27 
funcion4 = ((68.1 * 9.8) / x) * (1 - (E ** (-(x / 68.1) * 10))) - 40 
funcion5 = x ** 3 - 2 * x - 5 
mp.dps = 0
arregloIteracionesNewton = []
arregloIteracionesBiseccion = []
arregloTolerancia = ["10^-8", "10^-16", "10^-32", "10^-56"]

#impresion del menu de consola
print("---------------------------------------")
print("BISECCION")
valorABiseccion = input ("Ingrese el valor de inicio de la Biseccion: ")
valorBBiseccion = input ("Ingrese el valor de fin de la Biseccion: ")
print("---------------------------------------")
print("NEWTON")
valor = input("Ingrese el valor inicial para Newton: ")
print("---------------------------------------")
print("1) (cos(x))**2 - x ** 2")
print ("2) x sin(x) - 1 en [-1,2]")
print("3) x ** 3 - 2*(x**2) + ((4/3)*x) - 8/27")
print ("4) ((68.1 * 9.8) / x) * (1 - (E ** (-(x / 68.1) * 10))) - 40")
print ("5) x^3 - 2x - 5 = 0")
print("---------------------------------------")
numeroF = int(input("Ingrese la funcion que desea trabajar: "))

#asignacion del valor de la funcion 
funcion = None
if numeroF == 1:
    funcion = funcion1
elif numeroF == 2:
    funcion = funcion2
    valor = 1
elif numeroF == 3:
    funcion = funcion3
elif numeroF == 4:
    funcion = funcion4
elif numeroF == 5:
    funcion = funcion5


# ejecucion del codigo 
mp.dps = 8
print("---------------------------------------")
print("raiz = " + str(mpf(metodoNewton(mpf(valor), mpf(1.0e-8), funcion))))
print("raiz = " + str(mpf(metodoBiseccion(mpf(valorABiseccion),mpf(valorBBiseccion), mpf(1.0e-8), funcion))))
print("---------------------------------------")
mp.dps = 16
print("---------------------------------------")
print("raiz = " + str(mpf(metodoNewton(mpf(valor), mpf(1.0e-16), funcion))))
print("raiz = " + str(mpf(metodoBiseccion(mpf(valorABiseccion),mpf(valorBBiseccion), mpf(1.0e-16), funcion))))
print("---------------------------------------")
mp.dps = 32
print("---------------------------------------")
print("raiz = " + str(mpf(metodoNewton(mpf(valor), mpf(1.0e-32), funcion))))
print("raiz = " + str(mpf(metodoBiseccion(mpf(valorABiseccion),mpf(valorBBiseccion), mpf(1.0e-32), funcion))))
print("---------------------------------------")
mp.dps = 56
print("---------------------------------------")
print("raiz = " + str(mpf(metodoNewton(mpf(valor), mpf(1.0e-56), funcion))))
print("raiz = " + str(mpf(metodoBiseccion(mpf(valorABiseccion),mpf(valorBBiseccion), mpf(1.0e-56), funcion))))
print("---------------------------------------")

# graficacion
plt.plot(arregloTolerancia, arregloIteracionesBiseccion,'o--r')
plt.plot(arregloTolerancia, arregloIteracionesNewton,'o--b' )

plt.xlabel('Tolerancia')
plt.ylabel('Numero Iteraciones')
plt.title('Comparacion entre Biseccion y Newton')
  
plt.show()    

