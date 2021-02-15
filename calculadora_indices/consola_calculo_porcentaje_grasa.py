# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:19:11 2021

@author: Henao
"""
import calculadora_indices as calc

def ejecutar_calculo_porcentaje_grasa()->None:
    peso = float(input("Ingreso su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Escriba su edad en años: "))
    valor_genero = float(input("Si su genero es masculino, digite el valor 10.8 si es femenino ingrese 0: "))
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("Su porcentaje de grasa corporal es de: ", porcentaje_grasa, " %")
    
ejecutar_calculo_porcentaje_grasa()