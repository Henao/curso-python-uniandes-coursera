# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:06:07 2021

@author: Henao
"""

x1 = int(input("Ingrese el valor de x1: "))
x2 = int(input("Ingrese el valor de x2: "))
x3 = int(input("Ingrese el valor de x3: "))

temporal = x1
x1=x3
x3=x2
x2=temporal

print(str(x1) + ", " + str(x2) + ", " + str(x3))