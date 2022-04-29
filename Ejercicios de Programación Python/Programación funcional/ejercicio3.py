import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 3
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
li = [1, 2, 3, 4, "a"]


def fun(b):
    # print("Este es la otra función ")
    b = str(b)
    if b.isalpha():
        return " es un caracter string"
    else:
        return " es un caracter númerico"


def recibo(fun, li):
    print("Esta es la lista " + str(li))
    for i in li:
        print("El caracter "+str(i)+" es "+(fun(i)))
    print("\nSe terminaron los elementos de la lista")


recibo(fun, li)
