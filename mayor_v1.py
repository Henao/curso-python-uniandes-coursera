# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:10:03 2021

@author: Henao
"""
# num1 = int(input("Digite un número: "))
# num2 = int(input("Digite el segundo número: "))
# num3 = int(input("Digite el tercer número: "))
# num4 = int(input("Digite el cuarto número: "))

def mayor_v1(a: int, b: int, c: int, d: int)->int:
    if (a >= b) and (a >= c) and (a >= d):
        resultado = a
    elif (b >= a) and (b >= c) and (b >= d):
        resultado = b
    elif (c >= a) and (c >= b) and (c >= d):
        resultado = c
    else:
        resultado = d
        
    return resultado