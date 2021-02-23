# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:04:19 2021

@author: Henao
"""
num1 = int(input("Digite un número: "))
num2 = int(input("Digite el segundo número: "))
num3 = int(input("Digite el tercer número: "))

cuantos = 0
if (num1 % 2 == 0):
    cuantos += 1
if (num2 % 2 == 0):
    cuantos += 1
if (num3 % 2 == 0):
    cuantos += 1
    
print("De los tres  número digitados hay ", cuantos, " pares")