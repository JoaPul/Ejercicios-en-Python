import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla

# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def circulo(radio):
    global ac  # hace la variable global
    ac = 3.1416*radio**2
    print("\nEl área del circulo es de " +
          str(round(ac, 2))+' Unidades cuadradas')


def cilindro(altura):
    circulo(radio)
    volumen = ac*altura
    print('Este es el volumen obtenido del cilindro ' +
          str(round(volumen, 2))+' en Unidades cubicas')


radio = float(input('Dame el radio del circulo: '))
altura = float(input('Dame la altura del cilindro: '))
cilindro(altura)
