# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:36:39 2021

@author: Henao
"""
import math

x = int(input("Digite un número: "))

if x < 0:
    print("El número ", x, " no es válido aquí")
    y = x
    x = 42
    print(" Decidí usar el número 42 en lugar de ", y)
    
print("La raiz cuadrada de ", x, "es: ", math.sqrt(x))