import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

a = [2, 5, 6, 4, 8, 1]


def cuadrados(a):
    b = a
    print(a)
    for i in range(len(a)):
        b[i] = (a[i]**2)
    print(b)


cuadrados(a)
