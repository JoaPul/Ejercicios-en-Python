# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
# deberá aplicar un 21%.
import os
os.system("cls")  # se borra todo lo que se tenia en la pantalla


def fac(iva):
    pres = float(input("Dame la cantidad a pagar antes de impuestos: "))
    if iva == 0:
        total = .21*pres+pres
    else:
        total = iva*pres+pres
    print('Este es el total a pagar ' + str(total) + ' en MXN')


iva = float(
    input("Dame el porcentaje de IVA que deceas aplicar (en formato '.00'): "))
fac(iva)
