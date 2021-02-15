# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:18:34 2021

@author: Henao
"""
import calculadora_indices as calc

def ejecutar_calcular_imc()-> None:
    peso = float(input("Ingreso su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    print("Su indice de masa corporal es: ", imc)
    
ejecutar_calcular_imc()