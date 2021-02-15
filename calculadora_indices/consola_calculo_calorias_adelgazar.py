# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:20:28 2021

@author: Henao
"""
import calculadora_indices as calc

def ejecutar_calculo_calorias_adelgazar()->None:
    
    peso = float(input("Ingreso su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Escriba su edad en años: "))
    valor_genero = float(input("Si su genero es masculino, digite el valor  5 si es femenino ingrese -161: "))
    rango_calorias = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    
    print(rango_calorias)
    
ejecutar_calculo_calorias_adelgazar()