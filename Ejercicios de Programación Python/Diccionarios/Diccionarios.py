import os
import math
from typing import Counter

os.system("cls")  # se borra todo lo que se tenia en la pantalla

# # ejercicio 58 "Diccionarios" Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# a = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
# b = input("Dime que divisa utilizaras el día de hoy: ")
# b = b.title()  # Hace laprimera letra mayuscula
# if b in a:
#     print("\nHas escogido la divisa "+b+" y su simbolo es " + str(a[b]))
# else:
#     print("\nLa divisa "+b+" no se encuentra en el diccionario")

# # ejercicio 59 Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# a = {}
# a['Nombre'] = input("Dime tu nombre: ")
# a['Edad'] = input("\nDime tu edad: ")
# a['Dirección'] = input("\nDime tu dirección: ")
# a['Teléfono'] = input("\nDime tu teléfono: ")

# print('\n'+a['Nombre']+' tiene '+a['Edad']+' años, vive en ' +
#       a['Dirección']+' y su número de teléfono es '+a['Teléfono'])

# ejercicio 60 Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# a = {'Platáno': 1.35, 'Manzana': .8, 'Pera': .85, 'Naranja': .7}
# b = input('Que fruta deseas comprar?\n\n')
# print(a.get[b, "\nNo te venimos manejando esa fruta"]) Esta es otra forma de mostrar el mensaje de error
# if b in a:
#     c = float(input('\nCuantos kilos vas a querer?\n'))
#     d = (a[b])*c
#     print('\nTu total seria '+str(d))
# else:
#     print('\nEsa fruta no te la vengo manejando')

# ejercicio 61 Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
# a = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
#      8: 'Agosto', 9: 'September', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
# b = input('Dame una fecha con el siguiente formato dd/mm/aaaa: ')
# b = (b.split('/'))
# # print('\n'+str(b)) Comprobación de la fecha
# print('\n Esta es la fecha: '+str(b[0])+' de ' +
#       str(a[int(b[1])])+' del año de '+str(b[2]))

# ejercicio 62 Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
# a = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# for i in a:
#     b = i
#     print('\n'+i+' tiene '+str(a[i])+' creditos')

# ejercicio 63 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
# a = {}
# while True:
#     b = input('Que me vas a dar: ')
#     c = input('Damelo pues: ')
#     a[b] = c
#     print('Esto me has dado ' + str(a))
#     d = input(
#         'Escribe "n" si ya no vas a agregar nada, si deseas agregar algo, escribe otra cosa ')
#     d = d.lower()
#     if d == 'n':
#         break

# ejercicio 64 Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste

# a = {}
# e = 0
# while True:
#     b = input('Que me vas a dar: ')
#     c = float(input('Que precio tiene: '))
#     e = e+c
#     a[b] = c
#     d = input(
#         'Escribe "n" si ya no vas a agregar nada, si deseas agregar algo, escribe otra cosa ')
#     d = d.lower()
#     if d == 'n':
#         break

# print('Esto esta en tu carrito ' + str(a) +
#       ' y el total a pagar es de ' + str(e))

# ejercicio 65 Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
# a = {}
# d = []
# print("Hagamos un programa para traducir de Español a inglés")
# b = input('\nDame una palabra en español, despues escribe ":", \ncontinuando con la traducción en ingles, \ndespues introduciras una "," \npara seguir escribiendo tu diccionario: \n')
# b = b.split(',')
# # Papá:Dad,Come:eats,papa:potatoe
# for i in range(len(b)):
#     c = b[i].split(':')
#     a[c[0]] = c[1]

# c = input('\nDime una oración para traducir: \n')
# f = c
# c = c.split(' ')

# for i in range(len(c)):
#     e = 1
#     for j in a.keys():
#         if c[i] == j:
#             d.append(a[c[i]])
#             break
#         e = e+1
#         if e > len(a):
#             d.append(c[i])

# b = ''
# print('\nEsto es lo que pude traducir de \n'+f)
# for i in d:
#     b = b.__add__(i+' ')
# print(b)

# diccionario = {}
# palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
# for i in palabras.split(','):
#     clave, valor = i.split(':')
#     diccionario[clave] = valor
# frase = input('Introduce una frase en español: ')
# for i in frase.split():
#     if i in diccionario:
#         print(diccionario[i], end=' ')
#     else:
#         print(i, end=' ')

# ejercicio 66 Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
# print("Vamos a checar las facturas")
# a = {}
# pagar = 0.0
# while True:
#     b = input("\nQue quieres hacer?\nEscribe:\n1-Si deseas añadir una factura al diccionario\n2-Si deseas pagar una factura\nCualquier otro número- Si deseas salir del programa\n")
#     if b == "1":
#         c = int(input("Dame el número de factura que quisieras añadir "))
#         a[c] = float(input("Dame el precio de la factura "))
#         print(a)
#         for i in a:
#             total = 0
#             pagar = pagar+a[i]
#             total = total+a[i]
#         print("\nEste es el total a pagar: " + str(total) +
#               "\nEste es el total cobrado: "+str(pagar-total))
#     elif b == "2":
#         print(a)
#         d = int(input("Dame el número de factura que deceas eliminar: "))
#         del a[d]
#         print(a)
#         for i in a:
#             total = 0
#             total = total+a[i]
#         print("\nEste es el total a pagar: " + str(total) +
#               "\nEste es el total cobrado: "+str(pagar-total))
#     else:
#         break

# # respuesta de la pagina
# facturas = {}
# cobrado = 0
# pendiente = 0
# more = ''
# while more != 'T':
#     if more == 'A':
#         clave = input('Introduce el número de la factura: ')
#         coste = float(input('Introduce el coste de la factura: '))
#         facturas[clave] = coste
#         pendiente += coste
#     if more == 'P':
#         clave = input('Introduce el número de la factura a pagar: ')
#         coste = facturas.pop(clave, 0)
#         cobrado += coste
#         pendiente -= coste
#     print('Recaudado:', cobrado)
#     print('Pendiente de cobro: ', pendiente)
#     more = input(
#         '¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')


# ejercicio 67 Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.
# tupla = ()
# lista = []
# a = {}
# c = 0
# # print(type(lista), type(tupla))
# print("Hola que quieres hacer?")
# while True:
#     el = int(input("Elige:\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n\n"))
#     if el == 1:
#         b = {}  # limpia las variables que se vuelvan a utilizar
#         print("\nHas elegido AÑADIR CLIENTE")
#         b["Nombre"] = input("Dame entonces el nombre del cliente: ")
#         b["Dirección"] = input("Dame la dirección del cliente: ")
#         b["Teléfono"] = input("Dame el teléfono del cliente: ")
#         b["Correo"] = input("Dame el correo del cliente: ")
#         pre = input("\nEs un cliente preferente? y/n\n")
#         if pre == "y":
#             b["Preferente"] = True
#         else:
#             b["Preferente"] = False
#         a[c] = b
#         c += 1
#         # print(c)  # este se tiene que ir// prueba
#         # print(str(a)+'\n')  # este se tiene que ir// prueba
#     elif el == 2:
#         print("\nHas elegido ELIMINAR CLIENTE")
#         while True:
#             d = int(input("Dame el NIF del clente que deseas eliminar: "))
#             if d in a.keys():
#                 del a[d]
#                 print(
#                     "Este es el nuevo diccionario de los clientes que tenemos:", str(a))
#                 break
#             else:
#                 print("Ese cliente no existe intente otra vez ")
#     elif el == 3:
#         print("\nHas elegido MOSTRAR CLIENTES")
#         while True:
#             d = int(input("Dame el NIF del clente: "))
#             if d in a.keys():
#                 for i in a[d]:
#                     # asi podemos imprimir lo que hay adentro de un diccionario dentro de un diccionario
#                     print(str(i)+':'+str(a[d][i]))
#                     break
#                 else:
#                     print("Ese cliente no existe intente otra vez ")
#     elif el == 4:
#         print("\nHas elegido LISTAR TODOS LOS CLIENTES")
#         for i in range(len(a)):
#             print("\nNIF : "+str(i))
#             for j in a[i]:
#                 print(str(j)+' : '+str(a[i][j]))
#     elif el == 5:
#         print("\nHas elegido LISTAR TODOS LOS CLIENTES PREFERENTES")
#         for i in range(len(a)):
#             if a[i]["Preferente"] == True:
#                 print("\nNIF : "+str(i))
#                 for j in a[i]:
#                     print(str(j)+' : '+str(a[i][j]))
#     elif el == 6:
#         print("Programa terminado")
#         break

# ejercicio 68 El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.
#
