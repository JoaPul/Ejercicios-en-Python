import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 13
#a=input("Cual es tu nombre?\n")
#b=int(input("Cuantas veces se repertiera?"))
# c=1
# while c<=b:
# print(a)
# c=c+1

# ejercicio 14
#a=input("Dame tu nombre completo: ")
#print("Este es tu nombre en minusculas: " + a.lower())
#print("Este es tu nombre en MAYUSCULAS: " + a.upper())
#print("Este es tu nombre con las primeras letras de cada palabra en MAYUSCULAS: " + a.title())

# ejercicio 15
#a=input("Dame tu nombre: ")
# b=0

# for i in a:
#   if (i.isalpha()):
#      b=b+1

#print("Tu nombre es " + a.upper() + " y tiene " + str(b) + " letras")

# ejercicio 16
#a=input("Dame tu numer de telefono, \nque incluya los dos numeros de del codigo del pais, \ny los dos ultimos numeros de la extención \n(en total son 14 numeros):\n")
# b=0
# c=len(a)

# while b<=c:
#   if b>2 and b<13:
#      e=a[2:b]
#   b=b+1

# print(e)
#print("Este es la clave del pais al que pertenece tu telefono: +" + a[0:2])
#print("Este es tu numero de telefono (10 digitos): " + a[2:12])
#print("Esta es la extención de tu número de telefono: " + a[12:14])

# ejerccicio 17
#a=input("Dame una frase: ")
# print(a[::-1])# la primera parte dentro de los corchetes [a:b], a= de donde empieza a darte las letras, b= la posicion de la ultima letra que te va a dar, (: = todas)

# ejercicio 18
#a=input("Dame tu correo electronico: ")
# print("Te dare tu nombre de tu correo con el siguiente dominio: @ceu.es")
# b=(a.split('@')) #divide el string
# #print(b)
# #print(len(b))
# print(f"{b[0]}@ceu.es") #sustituye lo que va despues de @
#print(a[:a.find('@')] + '@ceu.es')

# ejercicio 19
# c=float(input("Dame el precio del producto: "))
# a=round(c,2)
# b=str(a)
# print('Son ' + b[:b.find(".")] +' con ' + b[b.find("."):])

# ejercicio 20
# a=input("Dame tu día de nacimiento en este formato dd/mm/aaaa: ")
# b=a.split('/')
# print(b)
# print('Ereas del día ' + a[:a.find('/')] + ' del mes ' + a[3:5] + ' y del año ' + a[6:10])
# print('Ereas del día ' + b[0] + ' del mes ' + b[1] + ' y del año ' + b[2])

# ejercicio 21
# a=input("Dame tu lista de compras separada por una coma: ")
# print(a.replace(',','\n'))

# ejercicio 22
b = input("Dame el nombre del Producto: ")
a = float(input("Dame el precio del producto: "))
c = int(input("Cuantas unidades del producto son: "))

print('Vas a comprar ' + b.upper() +
      ' con {c:3d} unidades, y un presio unitario de {a:9.2}. Dando un total de  {total:11.2}'.format(c=c, a=a, total=c*a))
