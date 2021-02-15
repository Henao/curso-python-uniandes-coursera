# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:57:45 2021

@author: Henao
"""
import math as m

def velocidad_final(altura: float)->float:
    vf = round((m.sqrt(2 * 9.8 * altura)),2)
    return vf

altura = float(input("Escriba la altura en metros desde la que cae el objeto: "))
print("La velocidad final del objeto es: ", velocidad_final(altura))