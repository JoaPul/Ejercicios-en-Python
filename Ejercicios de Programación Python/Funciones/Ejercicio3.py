import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.


def factorial(num):
    j = 1
    for i in range(1, num):
        j = j*(i+1)
        # print(num, j, i)
    print("El factorial de "+str(num)+" es "+str(j))


num = int(input("Dame un número entero "))
factorial(num)
