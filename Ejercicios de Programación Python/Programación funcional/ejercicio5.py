import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 5
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
frase = "Dale pues asi somos"
c = 0
dicc = {}


def creador(frase):
    lista = frase.split(" ")
    print(lista)
    for i in range(len(lista)):
        dicc[lista[i]] = len(lista[i])
    return dicc


print(creador(frase))
