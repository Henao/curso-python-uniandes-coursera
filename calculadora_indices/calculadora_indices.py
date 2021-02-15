# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:43:25 2021

@author: Henao
"""
def calcular_IMC(peso: float, altura: float)-> float:
    BMI = round(float(peso / (altura**2)),2)
    return BMI

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)->float:
    porcentaje_GC = round((1.2 * (calcular_IMC(peso, altura)) + 0.23 * edad - 5.4 - valor_genero),2)
    return porcentaje_GC
    
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float  )->float:
    TMB = round(((10*peso) + (6.25*(altura*100)) - (5*edad) + valor_genero),2)
    return TMB

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)->float:
    TMB_actividad_fisica = round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad,2)
    return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float)->str:
    
    rango_inferior = round((calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.80),2)
    rango_superior = round((calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.85),2)
    rangos_adelgazar = "Para adelgazar es recomendado que consumas entre: " + str(rango_inferior) + " y " + str(rango_superior) + "calorías al día. Siendo  " + str(rango_inferior) +" el rango inferior y " + str(rango_superior) + " el rango superior."
    
    return rangos_adelgazar
