# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:36:39 2021

@author: Henao
"""
x = int(input("Digite un número: "))

if x % 2 == 0:
    print(x, " es par")
    print("¿Sabía usted que el número 2 es el único número par que es primo?")
    
else:
    print(x, " es impar")
    print("Sabía usted que multiplicar dos números impares " + 
          "siempre da un resultado impar?")