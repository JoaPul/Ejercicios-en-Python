import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# ejercicio 33 "Bucles" Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# a=input("Dame una palabra: ")
# b="1234567890"
# for i in b: #for i in range(10):
#    print(a)

# ejercicio 34 Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
# a=int(input("Cual es tu edad?: "))
# for i in range(a):
#    print(str(i+1))

# ejercicio 35  Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# a=int(input("Dame un número entero positivo y te devuelvo los numeros pares que exista hasta ese número dados: "))
# for i in range(a):

#    if (i+1)%2==0:
#       print(str(i+1))

# ejercicio 36 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# a=float(input("Dame la cantidad que vas a invertir: "))
# b=int(input("Cuantos años tendras la inversión: "))
# c=float(input("A que porcentaje se pondra la inversión: "))
# for i in range(b):
#    d=a
#    a=a+(a*c)
#    print('En el año ' + str(i+1) + ' se tendra de inversion ganada de ' + str(round((a-d),2)) + ' y un capital redondeado de ' + str(round(a,2)))

# ejercicio 37 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

# a=int(input("Dame un número entero: "))
# b=''
# for i in range(a):
#    b=b.__add__('*')
#    print(b)

# ejercicio 38 Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
# for i in range(10):
#    for f in range(10):
#       print(str(i+1)+'x'+str(f+1)+'='+str((i+1)*(f+1)),end="\t")
#    print("")

# ejercicio 39 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# a=int(input("Dame un número entero: "))
# b=1
# c=str(b)
# for i in range(a):
#    print(c[::-1])
#    b=b+2
#    c=c.__add__(' '+str(b))

# n = int(input("Introduce la altura del triángulo (entero positivo): "))
# for i in range(1, n+1, 2):
#    for j in range(i, 0, -2):
#         print(j, end=" ")
#    print("")

# ejercicio 40 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# a='asdfjklñ'
# while True:
#    b=input("Dame la contraseña: ")
#    if b==a:
#       print("\nLa contraseña es correcta")
#       break
#    else:
#       print("\nLa contraseña es incorrecta, intentalo nuevamente\n")

# ejercicio 41 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
# a=int(input('Dame un número entero, para ver si es Primo: '))
# b=1
# for i in range(1,a,1):
#    if a%i==0:
#       b=b+1
#       if b>=3:
#          print('\n\tEl numero no es Primo')
#          break

# if b<=2:
#    print('\n\tEl número es Primo')

# ejercicio 42 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# a=input('Dame una palabra: ')
# b=a[::-1]
# for i in b:
#    print(i)

# ejercicio 43 Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
# a=input('Dame una Frase: ')
# a=a.lower()
# b=input("Dame una letra y te dire cuantas veces aparece en la frase que me diste: ")
# b=b.lower()
# c=0
# for i in a:
#    if i==b:
#       c=c+1

# print("En la Frase dada, se tiene que el número de repeticiones de la letra que se buscaba "+b+' son '+str(c))

# ejercicio 44 Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
# while True:
#     frase = input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)
