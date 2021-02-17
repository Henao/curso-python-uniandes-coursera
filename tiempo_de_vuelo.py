# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:06:58 2021

@author: Henao
"""

def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minuto: int, duracion_segundos: int)->int:
    
    segundo_llegada = (segundo_salida + duracion_segundos)%60
    output_segundo_llegada = (segundo_salida + duracion_segundos)//60
   
    minuto_llegada = (minuto_salida + duracion_minuto + output_segundo_llegada)%60
    output_minuto_llegada =(minuto_salida + duracion_minuto)//60
    
    hora_llegada = (hora_salida + duracion_horas + output_minuto_llegada) % 24
    
    
    
    return hora_llegada, minuto_llegada, segundo_llegada