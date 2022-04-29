import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

a = [2, 3, 5, 4, 8, 2]


def media(a):
    c = 0
    for i in a:

        c = c+i

    i = c/len(a)
    print('Aqui yace tu media'+str(i))


media(a)
