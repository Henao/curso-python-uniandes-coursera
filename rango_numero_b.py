# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:06:20 2021

@author: Henao
"""
def rango_numero_b(numero: int)->int:
    if numero < 0:
        resultado = -1
    elif numero < 1000:
        resultado = 0
    elif numero <= 10000:
        resultado = 1
    else:
        resultado = 2
    return resultado


numero = int(input("Por favor ingrese un número entero: "))
print("El resultado es: ", rango_numero_b(numero))