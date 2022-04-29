import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# ejercicio 23 "Condicionales"
#a=int(input("Dime tu edad y te dire si eres mayor de edad: "))
# if a>18:
#    print("Eres mayor de edad")
# else:
#    print("No eres mayor de edad")

# ejercicio 24
# a="asdfjklñ"
# i=0
# while i==0:
# b=input("Dame la contraseña: ")
# b=b.lower()
# if b==a:
#    print("La contraseña es correcta")
#    break
# else:
#    print("La contraseña es incorrecta")

# ejercicio 25
# a=float(input("Vamos a hacer una división, dame el dividendo: "))
# b=float(input("Dame el Divisor: "))

# while b==0:
#    b=float(input("Error, ese divisor no esta permitio, por favor elige otro: "))

# print("Este es el resultado de la división: " + str(a/b))

# ejercicio 26 "Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."
# a=int(input("Vamos a jugar, si me das un número entero te dire si ese número es par o inpar\n"))
# c,r = divmod(a,2) #'r' es el residuo de la división, 'c' es el cociente, tabien se puede con a%2==0
# if r==0:
#    print("Es un número par")
# else:
#    print("Es un Número impar")

# ejercicio 27 'Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.'
# print('Para tributar se tiene que cumplir con 2 requisitos;\n-Tener una edad minima de 16 años\n-Tener un sueldo mensual minimo de $1000\nCumples con estos requisitos?')
# a=int(input("Dime tu edad: "))
# b=float(input("Dime tu salario persivido: "))
# if a>=16 and b>=1000:
#    print('Cumples con los requisitos, si tienes que tributar')
# else:
#    print('No cumples con todos los requisitos, no tienes que tributar')

# ejercicio 28 'Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'
# print("Vamos a averiguar a que grupo perteneces\n")
# a=input("Por favor indicame si eres mujer escribiendo 'M' o si eres Hombre escribe 'H'\n") #verificar que sean mayusculas
# a=a.upper()
# b=input("Como te llamas: ") #verificar la primera letra
# b=b[0].lower()
# c=('abcdefghijkl')
# f=('abcdefghijklm')
# e=('mnñopqrstuvwxyz')
# j=0
# while j==0:
#    for i in c:
#       d=i
#       if b==d and a=='M':
#          print("Estas en el grupo A")
#          j=1
#          break
#    for i in f:
#       d=i
#       if b==d and a=='H':
#          print('Eres del grupo A')
#          j=1
#          break
#    for i in e:
#       d=i
#       if b==d:
#          print("Estas en el grupo B")
#          j=1
#          break

# ejercicio 29 Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# a=float(input("Dime cual es tu renta anual: "))
# if a<10000:
#    b=5
# if a>=10000 and a<20000:
#    b=15
# if a>=20000 and a<35000:
#    b=20
# if a>=35000 and a<60000:
#    b=30
# if a>=60000:
#    b=45
#print("Lo que tienes que pagar es " + str(a*(b/100)+a) + '$')

# ejercicio 30 En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# a=float(input('Cual es el puntaje que le daras al empleado, \n(solo se pueden poner las siguientes calificaciones 0.0, 0.4, 0.6 o más): '))
# d=2400
# if a==0:
#    e=' Inaceptable '
# elif a==.4:
#    e=' Aceptable '
# elif a>=.6:
#    e=' Meritorio '
# print('De a cuerdo a tu nivel de rendimiento ' + str(a) + e + 'en total el dinero extra ganado es: $' + str(a*d))

# ejercicio 31 Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
# a=int(input("Dame tu edad: "))
# if a<4:
#    b=0
# if a>=4 and a<18:
#    b=5
# if a>=18:
#    b=10
# print('Si tu edad es '+ str(a) + ' entonces tienes que pagar $' + str(b))

# ejercicio 32 La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

# a=('Pimiento','Tofu')
# b=('Peperoni','Jamon','Salmón')
# while True:
#    c=input('Quieres una pizza vegetariana? (y/n): ')
#    if c == 'y':
#       print("Ingredientes de pizzas vegetarianas\n\tP- Pimiento\n\tT- Tofu\n")
#       while True:
#          d=input("\nQue deseas elegir: ")
#          d=d.upper()
#          if d=='P':
#             d=a[0]
#             break
#          elif d=='T':
#             d=a[1]
#             break
#          else:
#             print('Esta no es una opción\n ')
#       break
#    elif c=='n':
#       print("Ingredientes de pizzas no vegetarianas\n\tP- Peperoni\n\tJ- Jamón\n\tS- Salmón\n")
#       while True:
#          d=input("\nQue deseas elegir: ")
#          d=d.upper()
#          if d=='P':
#             d=a[0]
#             break
#          elif d=='J':
#             d=a[1]
#             break
#          elif d=='S':
#             d=a[2]
#             break
#          else:
#             print('Esta no es una opción\n ')
#       break
#    else:
#       print('Esa no es una opción\n ')
# print('Perfecto tu pizza traera Mozzarella, Tomate y ' + str(d))
