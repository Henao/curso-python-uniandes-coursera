# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:44:03 2021

@author: Henao
"""
def rango_numero(numero: int)->int:
    if numero < 0:
        resultado = -1
    if (numero > 0 and numero < 1000):
        resultado = 0
    if (numero >= 1000 and numero <= 10000 ):
        resultado = 1
    if numero > 10000:
        resultado = 2
    return resultado


numero = int(input("Por favor ingrese un número entero: "))
print("El resultado es: ", rango_numero(numero))