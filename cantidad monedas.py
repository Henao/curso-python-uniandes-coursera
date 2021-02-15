# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:54:21 2021

@author: Henao
"""
''' Según el reto:
def calcular_cambio(cambio: int)-> str:
    cantidad_A = cambio // 500
    cambio = cambio - (cantidad_A *500)
    cantidad_B = cambio // 200
    cambio = cambio - (cantidad_B *200)
    cantidad_C = cambio // 100
    cambio = cambio - (cantidad_C *100)
    cantidad_D = cambio // 50
    cantidad_monedas = str(cantidad_A) + "," + str(cantidad_B) + "," + str(cantidad_C) + "," + str(cantidad_D)

    return cantidad_monedas

'''
def calcular_cambio(cambio: int)-> str:
    cantidad_A = cambio // 500
    cambio = cambio - (cantidad_A *500)
    cantidad_B = cambio // 200
    cambio = cambio - (cantidad_B *200)
    cantidad_C = cambio // 100
    cambio = cambio - (cantidad_C *100)
    cantidad_D = cambio // 50
    cambio_monedas = str(cantidad_A) + " monedas de 500, " + str(cantidad_B) + " monedas de 200, " + str(cantidad_C) + " monedas de 100, " + str(cantidad_D) + " monedas de 50 "
    return cambio_monedas

cambio = int(input("Ingrese el valor del cambio a entregar: "))
print("El cambio para el cliente en la menor cantidad de monedas posible es: ", calcular_cambio(cambio))
