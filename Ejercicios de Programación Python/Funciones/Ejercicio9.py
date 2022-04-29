import os
import math
os.system("cls")  # se borra todo lo que se tenia en la pantalla
# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

a = 24
b = 36


def divisores(a, b):
    pl = []
    sl = []
    mcd = []
    if a > b:  # aqui inicia a calcular el MCD
        may = a
    else:
        may = b
    for i in range(1, may+1):
        if a % i == 0:
            pl.append(i)
        if b % i == 0:
            sl.append(i)
    for j in pl:
        for i in sl:
            if j == i:
                mcd.append(j)
    print("De los números "+str(a)+" y "+str(b))
    print('Aqui esta nuestro maximo comun divisor '+str(mcd[-1]))
    # print(pl, sl)
    pl = []
    sl = []
    while True:
        for i in range(2, may+1):  # aqui empezamos a buscar nuestro minimo comun multiplo
            if a % i == 0:
                a = int(a/i)
                pl.append(i)
                break
            if b % i == 0:
                b = int(b/i)
                may = b
                sl.append(i)
                break
        if may == 1:
            break
    # print(pl, sl)
    dica = {}
    dicb = {}
    # aqui empezamos a buscar cuantas veces se repite un número en las lista
    for i in range(len(pl)):
        if i != len(pl)-1 and pl[i] == pl[i+1]:
            may = may+1
            dica[pl[i]] = may
        elif i != 0 and pl[i] == pl[i-1]:
            may = 1
        else:
            may = 1
            dica[pl[i]] = may
    may = 1
    for i in range(len(sl)):
        if i != len(sl)-1 and sl[i] == sl[i+1]:
            may = may+1
            dicb[sl[i]] = may
        elif i != 0 and sl[i] == sl[i-1]:
            may = 1
        else:
            may = 1
            dicb[sl[i]] = may
            # print(dicb, i, len(sl), sl)
    # print(dica, dicb)
    if a > b:  # aqui inicia a calcular el mayor entre a y b
        dicc = dicb
        dicb = dica
        dica = dicc
    pl = list(dica.keys())
    sl = list(dicb.keys())
    # print(pl, sl)
    mcm = 1
    # aqui se genera un diccionario con los valores a multiplicar para obtener mcm
    for i in range(len(dica)):
        for j in range(len(dicb)):
            if pl[i] == sl[j]:
                if dica[pl[i]] >= dicb[sl[j]]:
                    dicb[sl[j]] = dica[pl[i]]
    for i in range(len(dicb)):  # aqui se calcula el mcm
        mcm = mcm*(sl[i]**dicb[sl[i]])

    # print(dicb)

    print('El minimo comun multiplo es  '+str(mcm))

    # print(dica.get(6, False))


divisores(a, b)

# def mcd(n, m):
#     """Función que calcula el máximo común divisor de dos números.
#     Parámetros:
#         - n: Es un número entero.
#         - m: Es un número entero.
#     Devuelve:
#         El máximo común divisor de n y m.
#     """
#     rest = 0
#     while(m > 0):
#         rest = m
#         m = n % m
#         n = rest
#     return n

# def mcm(n, m):
#     """Función que calcula el mínimo común múltiplo de dos números.
#     Parámetros:
#         - n: Es un número entero.
#         - m: Es un número entero.
#     Devuelve:
#         El mínimo común múltiplo de n y m.
#     """
#     if n > m:
#         greater = n
#     else:
#         greater = m
#     while (greater % n != 0) or (greater % m != 0):
#         greater += 1
#     return greater

# print(mcd(24,36))
# print(mcm(24,36))
