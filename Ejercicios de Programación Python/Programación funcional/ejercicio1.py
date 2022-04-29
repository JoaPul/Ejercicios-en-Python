import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla
# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

dic = {100: 15, 200: 10, 400: 16}
l = list(dic.keys())


def descuento(precio, des):
    precio = precio-precio*(des/100)
    print("El total de la compra con descuento es " + str(precio))


def IVA(precio, iva):
    precio = precio+precio*(iva/100)
    print("El total de la compra con iva es " + str(precio))


def cesta(dic):
    for i in range(len(dic)):
        precio = l[i]
        if dic[l[i]] == 16:
            iva = dic[l[i]]
            IVA(precio, iva)

        else:
            des = dic[l[i]]
            descuento(precio, des)


cesta(dic)
