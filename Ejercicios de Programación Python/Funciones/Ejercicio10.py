import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

a = int(input("Dame una número en base diez para que lo pueda transformar en binario: "))


def binario(a):
    bina = ''
    while True:
        for i in range(a):
            if a % 2 == 0:
                bina = bina+'0'
                a = int(a/2)
                break
            else:
                bina = bina+'1'
                a = int(a-1)/2
        if a == 0:
            if bina[-1] == '0':
                bina = bina[0:-1]
            break

    print('Este es el valor en binarios: '+bina[::-1])


binario(a)

b = (input("Dame una número binario para pasarlo a decimal: "))


def decimal(b):
    b = b[::-1]
    c = 0
    for i in range(len(b)):
        if b[i] == '1':
            c = c+2**i
    print('Este es el valor en decimal: '+str(c))


decimal(b)
