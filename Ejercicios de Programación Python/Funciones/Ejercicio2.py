import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla

#Ejercicio 2
#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.


def Hola(nom):
    print("Hola "+nom)

nom=input("Dame tu nombre: ")
Hola(nom)