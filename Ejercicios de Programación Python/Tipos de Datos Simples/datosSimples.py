import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# ejercicio 1
#print("¡Hola Mundo!")

# ejercicio 2
#a="¡Hola Mundo!"
# print(a)

# ejercicio 3
#print("Cual es tu nombre? \n")
#nombre=input ("Cual es tu nombre? \n :")
#print("¡Hola " + nombre + "!")

# ejercicio 4
# b=((3+2)/(2*5))**2
# a=round(b,2)
#print("El resultado de la siguiente operacion es: \n")
# print(b)

# ejercicio 5
#a=float(input ("Cuantas horas trabajas a la semana? \n"))
#b=float(input ("cuanto te pagan la hora? (valor decimal expresado en MXN) \n"))
# d=a*b
# c=round(d,2)
#print("Este es tu salario semanal: ", c)

# ejercicio 6
#a=int(input("Dame un número entero \nPara poder regresate la suma de todos los enteros \ndesde el 1 hasta el número que me hayas dado\n"))
# b=((a*(a+1))/2)
#print("este es el resultado de la suma \n" + str(b))

# ejercicio 7
#a=float(input("Dame tu peso en Kg \n"))
#b=float(input("Dame tu estatura en m\n"))
# c=round(((a)/(b**2)),2)
#print("Tu IMC es: " + str(c) + " kg/m^2")

# ejercicio 8
#print("Vamos a hacer una división, \nasi te podre decir las parte de ella")
#n=float(input("Dame el primer número: "))
#m=float(input("Dame el segundo número: "))
#c,r = divmod(n,m)
#print("Cociente: {}, reciduo: {}".format(c,r))

# ejercicio 9
#a=float(input("Cantidad a invertir (expresados en MXN): "))
#b=float(input("Cual sera el interes anual (expresado en porciento decimal): "))
#c=float(input("Cual es la cantidad de años que se estara invirtiendo (expresados en enteros con punto decimal): "))
# d=((a*b)*c) #capital ganado por inversion
# e=(d+a) #capital inicial
# f=b*100
#print("Este ha sido tu capital inicial $"+ str(a)+ "\nLo hemos puesto como inversion a un interes anual de " + str(f) + "%\nEstos son el número de años en los cuales se mantubo activa la inversión " + str(c) + "Años\nEste es el dinero ganado $" + str(d) + "\nY este es el capital actual que se obtuvo $" + str(e))

# ejercicio 10
# p=.112
# m=.75
#a=float(input("Cuantos payasos van en el Paquete?\n"))
#b=float(input("Cuantas muñecas van en el paquete\n"))
# c=round(a*p+b*m,2)
#print("Este es el total de peso que habra en el paquete " + str(c) + "Kg")

# ejercicio 11
#a=float(input("Cual es tu saldo actual en tu cuenta de ahorros? (expresado en MXN) : $"))
# b=.04
# e=round(a,2)
# for c in [1,2,3]:
#   d=(a*b+e)
#  e=round(d,2)
# print("Para el año " + str(c) + "tu saldo en tu cuenta de ahorros es de: $" + str(e))

#print("Al inicio de tu inversión tenias un capital de $" + str(round(a,2)) + "\nDespues de la inverción, tu capital es de $" + str(e))

# ejercicio 12
# a=3.49
# b=.6
#c=float(input("Cuantos panes que no son del dia se vendieron hoy?\n"))
# p=round(a*c,2)
# d=round(a*b*c,2)
# t=round((c*a)*(1-b),2)#precio de panes que no son del dia
#print("El total de panes vendidos que no son del día son: " + str(c) + " Unidades\nEl precio total por la compra es de : $" + str(p) + "\nEl descuento que se le haria a estos panes es de: $" + str(d) + "\nEl total a pagar es de: $"+ str(t))

# ejercicico fibonachi
#print("Programa de fibonacci")
#a=int(input("Dime que posición de la sucesión de fibonacci quieres saber su valor: "))

# def fibonacci(a):
#   b=3
#   c=0
#   d=1
#   e=0

#   if a==1:
#      print("El valor que tiene la posición del ciclo de fibonacci " + str(a) + " es " + str(c))
#   else:
#      if a==2:
#         print("El valor que tiene la posición del ciclo de fibonacci " + str(a) + " es " + str(d))
#      else:
#         while b<=a:
#            e=c+d
#            c=d
#            d=e
# print(str(b) +"="+str(e)) #verificador de posición
#            b=b+1
#         print("El valor que tiene la posición del ciclo de fibonacci " + str(a) + " es " + str(e))

# fibonacci(a)

# ejercicico fibonachi con pregunta de volver a intentarlo
# def fibonacci(a):
#   a=int(input("Dime que posición de la sucesión de fibonacci quieres saber su valor: "))
#   b=1
#   c=0
#   d=1
#   e=0
#   x=0
#   while b<=a:
#      e=c+d
#      x=c
#      c=d
#      d=e
#      b=b+1
#      print(str(b-1) +"="+str(x)) #verificador de posición
#   print("El valor que tiene la posición del ciclo de fibonacci " + str(a) + " es " + str(x))

# def retake(f):
#  while f==1:
#     fibonacci(a)
#     f=int(input("\nQuieres saber el valor de otra posición? \n(Escribe 1 para si, o escribe cualquier otra cosa para no)\n"))
#  print("Ok buen día")


#print("Programa de fibonacci")
# a=1
# f=1
# retake(f)
