import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# ejercicio 45 Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# a=input("Dame las asignaciones del curso que tomaras separadas por una coma(,): ")
# print(a.split(','))

# ejercicio 46 Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
# a=('Mate','Español','Geografia','Historia')
# b=0
# for i in a:
#    print('Estudio la materia '+ a[b])
#    b=b+1

# ejercicio 47 Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
# a=('Matemáticas','Física','Química','Historia','Lengua')
# c=0
# d=list(a) #se cambia de tuple a lista
# for i in a:
#    b=(input('Dame la calificación de '+a[c]+' '))
#    d[c]=b
#  #  print(d)
#    c=c+1
# b=tuple(d)
# os.system ("cls") # os es una funcion que te deja escribir en la terminal desde el programa
# c=0
# for i in a:
#    print('En '+i+'has sacado '+b[c])
#    c=c+1

# ejercicio 48 Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# b=[] #con corchetes[] se vuelven listas, pueden tener int, Float o str
# e=0
# def menor():
#    for i in range(0,len(b)-1):# ciclo para contar las veces que se repetira el ciclo de evalución
#       for j in range(0,len(b)-1):#ciclo para hacer la comparación de cada número
#          if b[j]>b[j+1]:
#             aux=b[j]
#             b[j]=b[j+1]
#             b[j+1]=aux


# while e==0:
#    while True:
#       a=(input('\nDame un número ganador de la loteria: '))
#       if a.isnumeric()==True:
#          break
#       else:
#          print('\nEsa madre no es un número\n')
#    b.append(a)
#    while True:
#       d=input('\nAun te quedan números para darme (y/n): ')
#       d=d.lower()
#       if d=='y':
#          print('Dale pues\n')
#          break
#       elif d=='n':
#          print('\n\n\tEsta es la lista que me mandaste\n\n'+str(b))
#          print('\n\n\tAqui estan los números gandores de menor a mayor\n')
#          menor()
#          print(b)
#          e=1
#          break
#       else:
#          print('No te entendi ni madres.\n')


# awarded = []
# for i in range(6):
#     awarded.append(int(input("Introduce un número ganador: ")))
# awarded.sort()
# print("Los números ganadores son " + str(awarded))

# ejercicio 49 Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
# a=[]
# b=0
# for i in range(10):
#    b=b+1
#    a.append(b)
# for j in range(1,11):
#    print(a[-j], end=',')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, 11):
#     print(numbers[-i], end=", ")

# ejercicio 50 Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
# a=['Matemáticas','Física','Química','Historia','Lengua']
# c=[]
# d=[]
# for i in a:
#    b=int(input("Cual es la calificacion que sacaste en "+i+ ' '))
#    c.append(b)

# for i in range(0,len(c)):
#    if c[i]>5:
#       d.append(a[i])

# print('Estas son las materias que tienes con calificación aprobatoria \n' + ', '.join(d)) #'.join' deja imprimir una lista sin corchetes.

# Ejercicio 51 Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
# a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# d=a
# b=9
# print('Esta es la lista del abecedario : ' + ','.join(a))
# for i in d:
#    c=b*3
#    b=b-1
#    #print(b,c-1)
#    if c==0:
#       break
#    d.remove(d[c-1])

# #print('Esta es la lista del abecedario : ' + ','.join(a)) # si pongo aqui esta print, aun no se porque, pero hace que a=d
# print('\nEsta es la lista del abecedario sin las letras que estan en las posisiones con que son multiplos de 3: '+ ','.join(d))

# ejercicio 52 Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
# a=input('Dame una palabra: ')
# b=a[::-1]
# if b==a:
#    print('Tienea un palindromo')
#    print(a, b)
# else:
#    print('Este no es un palindromo')
#    print(a, b)

# ejercicio 53 Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
# a=input('Dame una palabra: ')
# a=a.lower()
# print('La vocal "a" se repite '+ str(a.count('a')))
# print('La vocal "e" se repite '+ str(a.count('e')))
# print('La vocal "i" se repite '+ str(a.count('i')))
# print('La vocal "o" se repite '+ str(a.count('o')))
# print('La vocal "u" se repite '+ str(a.count('u')))

# word = input("Introduce una palabra: ")
# vocals = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocals:
#     times = 0
#     for letter in word:
#         if letter == vocal:
#             times += 1
#     print("La vocal " + vocal + " aparece " + str(times) + " veces")

# ejercicio 54 Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
# a=[50, 75, 46, 22, 80, 65, 8]
# for j in range(0,len(a)-1):
#    for i in range(0,len(a)-1):
#       if a[i]>a[i+1]:
#          b=a[i]
#          a[i]=a[i+1]
#          a[i+1]=b
# print('Este es el número mas grande '+str(a[-1]))
# print('Este es el númeto mas pequeño '+str(a[0]))

# ejercicio 55 Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
# a=[1,2,3]
# b=[-1,0,2]
# d=0
# for i in range(len(a)):
#    c=a[i]*b[i]
#    d=d+c
# print('Este es el producto escalar de los vectores '+str(a)+' y '+str(b)+' que da como resultado '+str(d))

# ejercicio 56 Escribir un programa que almacene las matrices a=[1,2,34,5,6] y b=[-1,00,11,1]
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
# a = ((1, 2, 3),
#      (4, 5, 6))
# b = ((-1, 0),
#      (0, 1),
#      (1,1))
# result = [[0,0],
#           [0,0]]
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             result[i][j] += a[i][k] * b[k][j]
# for i in range(len(result)):
#     result[i] = tuple(result[i])
# result = tuple(result)
# for i in range(len(result)):
#     print(result[i])

# ejercicio 57 Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
# a=input('Dame números separados por comas: ')
# a=a.split(',')
# print(a)
# b=0
# s=0
# for i in range(len(a)):
#    b=b+(int(a[i]))
#    #print(b, i)
# b=b/(i+1) #media calculada
# print('\n Esta es la media de los números que me diste: '+str(b))

# for i in a:
#    s=s+((int(i))-b)**2
# r=(s/(len(a)+1))**(1/2) #desviación estandar calculada
# print('\n Y aqui podras observar que la mayoria de los datos estan a '+str(round(r,2))+' unidades de distancia de nuestra media '+str(b))
