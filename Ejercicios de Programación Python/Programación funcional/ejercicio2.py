import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.


def se():
    num = float(input("Dame el número al que le quieres sacar el seno: "))
    res = math.sin(num)
    print("El resultado es "+str(round(res, 2)))


def co():
    num = float(input("Dame el número al que le quieres sacar el coseno: "))
    res = math.cos(num)
    print("El resultado es "+str(round(res, 2)))


def ta():
    num = float(input("Dame el número al que le quieres sacar la tangente: "))
    res = math.tan(num)
    print("El resultado es "+str(round(res, 2)))


def ex():
    num = float(input("Dame el número al que quieres elevar la base: "))
    bas = float(input("Dame el número que funcionara como la base: "))
    res = bas**num
    print("El resultado es "+str(round(res, 2)))


def lo():
    num = float(
        input("Dame el número al que le quieres sacar el logaritmo base 10: "))
    res = math.log10(num)
    print("El resultado es "+str(round(res, 2)))


while True:
    a = input(
        "Dime que funcion quieres realizar: \n1-Seno\n2-Coseno\n3-Tangente\n4-exponencial\n5-Logaritmo\n")
    if a == "1":
        se()
        break
    elif a == "2":
        co()
        break
    elif a == "3":
        ta()
        break
    elif a == "4":
        ex()
        break
    elif a == "5":
        lo()
        break
    else:
        print("\nEsa opción no es valida por favor elige otra opción\n")
