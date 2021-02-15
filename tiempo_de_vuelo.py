# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:06:58 2021

@author: Henao
"""

def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minuto: int, duracion_segundos: int)->int:
    
    segundo_llegada = ((segundo_salida + duracion_segundos)-60)%60
   
    minuto_llegada = minuto_salida + duracion_minuto
    hora_llegada = hora_salida + duracion_horas
    
    return hora_llegada, minuto_llegada, segundo_llegada