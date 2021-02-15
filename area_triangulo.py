# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:41:19 2021

@author: Henao
"""
import math 
def area_triangulo(s1: float, s2: float, s3: float)->float:
    '''Parameters
    ----------
    s1 : float
        Primer Lado del triangulo
    s2 : float
        Segundo Lado del triangulo
    s3 : float
        Tercer Lado del triangulo

    Returns
    ----------
    float
    
    El area del triangulo a partir del subperimetro s = (s1+s2+s3)/2 
    '''
    s=(s1+s2+s3)/2
    area = round(math.sqrt(s * (s-s1) * (s-s2) * (s-s3)),1)
    return area

s1 = float(input("Escriba el valor para el primer lado: "))
s2 = float(input("Escriba el valor para el segundo lado: "))
s3 = float(input("Escriba el valor para el tercer lado: "))

print("El area del triangulo es: " , area_triangulo(s1,s2,s3))

