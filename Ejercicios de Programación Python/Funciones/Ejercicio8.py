import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

a = [17, 15, 23, 7, 9, 13]


def esta(a):
    b = {}
    c = 0
    d = 0
    for i in a:  # media
        c = c+i
    i = c/len(a)
    b['media'] = round(i, 2)
    c = 0
    for j in a:  # desviación
        c = c+(j-i)**2
    d = (c)/len(a)
    j = math.sqrt(d)
    b['desviación estandar'] = round(j, 2)
    d = (c)/(len(a)-1)  # varianza
    b['varianza'] = round(d, 2)
    print(b)


esta(a)
