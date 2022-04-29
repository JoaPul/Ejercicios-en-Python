import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 4
# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

li = [1, 2, 3, 4, "a"]
lin = []


def fun(b):
    print("\nEl elemento "+str(b)+" es un número?")
    b = str(b)
    if b.isalpha():
        print("False")
        return False
    else:
        print("True")
        return True


def recibo(fun, li):
    print("Esta es la lista " + str(li))
    for i in li:
        lin.append(fun(i))
    print(lin)


recibo(fun, li)
