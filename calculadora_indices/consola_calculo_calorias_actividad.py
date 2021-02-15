# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:19:55 2021

@author: Henao
"""
import calculadora_indices as calc

def ejecutar_calculo_calorias_actividad()->None:
    peso = float(input("Ingreso su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Escriba su edad en años: "))
    valor_genero = float(input("Si su genero es masculino, digite el valor 5 si es femenino ingrese -161: "))
    valor_actividad = float(input("""
    Dependidendo de la actividad física semanal realizada:
        • 1.2: poco o ningún ejercicio
        • 1.375: ejercicio ligero (1 a 3 días a la semana)
        • 1.55: ejercicio moderado (3 a 5 días a la semana)
        • 1.725: deportista (6 -7 días a la semana)
        • 1.9: atleta (entrenamientos mañana y tarde)
    Ingrese un valor: 
    """))
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print("La cantidad de calorías que usted quema al realizar algún tipo de actividad física semanalmente es:  ", calorias_actividad, " calorias")
        
ejecutar_calculo_calorias_actividad()