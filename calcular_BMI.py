# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:42:24 2021

@author: Henao
"""

def calcular_BMI(peso_en_libras: float, estatura_en_pulgadas: float)-> float:
    '''
    Algorithm to calculate the body mass from your weight in pounds and your height in inches.
    Parameters
    ----------
    peso_en_libras : float
        Weight in pounds
    estatura_en_pulgadas : float
        Height in inches


    Returns
    ----------
    float
    
    BMI: your body mass index  
    
    '''
    peso = peso_en_libras * 0.45
    altura = estatura_en_pulgadas * 0.025
    BMI = round(float(peso / (altura**2)),2)
    return BMI
    
    
peso_en_libras = float(input("Enter your weight in pounds : "))
estatura_en_pulgadas = float(input("Enter your height in inches: "))

print("Your body mass index is: " , calcular_BMI(peso_en_libras, estatura_en_pulgadas))