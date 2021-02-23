# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:14:43 2021

@author: Henao
"""

def es_divisible(n: int, d:int)->int:
    if  d != 0 and n % (2*d) == 0:
        resultado = 2
    elif  d != 0 and (n % d == 0) and (n % (2*d) != 0):
        resultado = 1
    else:
        resultado = 0
    return resultado
            
  
        