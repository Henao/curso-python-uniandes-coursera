# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:22:41 2021

@author: Henao
"""
def son_colineales(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int)->bool:
    if ((y2 -y1) / (x2-x1)) == ((y3-y2) / (x3 -x2)):
        resultado = True
    else:
        resultado = False
    return resultado

def son_colineales_v2(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int)->bool:
    pendiente1 =  (y2 -y1) / (x2-x1)
    pendiente2 = (y3-y2) / (x3 -x2)
    if pendiente1 == pendiente2:
        resultado = True
    else:
        resultado = False
    return resultado

def son_colineales_v3(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int)->bool:
    pendiente1 =  (y2 -y1) / (x2-x1)
    pendiente2 = (y3-y2) / (x3 -x2)
    
    resultado = False
    if pendiente1 == pendiente2:
        resultado = True
    return resultado

def son_colineales_v4(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int)->bool:
    pendiente1 =  (y2 -y1) / (x2-x1)
    pendiente2 = (y3-y2) / (x3 -x2)
   
    return pendiente1 == pendiente2