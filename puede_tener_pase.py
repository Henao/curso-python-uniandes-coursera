# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:42:52 2021

@author: Henao
"""
def puede_tener_pase_v1(edad: int)->bool:
    if not (edad >= 16):
        respuesta = False
    else:
        respuesta = True
    return respuesta

def puede_tener_pase_v2(edad: int)->bool:
    if (edad < 16):
        respuesta = False
    else:
        respuesta = True
    return respuesta
        
def puede_tener_pase_v3(edad: int)->bool:
    puede = True
    if (edad < 16):
        puede = False
    return puede
    
def puede_tener_pase_v4(edad: int)->bool:
    puede = False
    if (edad >= 16):
        puede = True
    return puede
    
def puede_tener_pase_v5(edad: int)->bool:
    return (edad >= 16)