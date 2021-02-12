# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:06:05 2021

@author: Henao
"""

capital = float(input("Intruduzca el capital inicial: "))
tasa_interes = float(input("Intruduzca el porcentaje de interes: "))
anios = float(input("Ingrese el número de años: "))

valor_futuro = capital * (1+(tasa_interes/100))**anios
print("El valor futuro del monto inicial es de $" + str(round(valor_futuro, 2)) + ", transcurrido " + str(round(anios)) + " Años")
