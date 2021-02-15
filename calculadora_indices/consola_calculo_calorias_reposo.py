# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:19:41 2021

@author: MSI
"""
import calculadora_indices as calc

def ejecutar_calculo_calorias_reposo()->None:
    peso = float(input("Ingreso su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Escriba su edad en años: "))
    valor_genero = float(input("Si su genero es masculino, digite el valor 5 si es femenino ingrese -161: "))
    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorías que usted quema en reposo es de: ", calorias_reposo, " calorias")
        
ejecutar_calculo_calorias_reposo()