# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:36:38 2021

@author: Henao
"""
def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual:int, anio_actual:int)->int:
    anio_def = (anio_actual - anio_nacio)*365
    mes_def = (mes_actual - mes_nacio)*30
    dia_def = dia_actual - dia_nacio
    dias_total = anio_def + mes_def + dia_def
    anio = dias_total // 365
    dias_total = dias_total - (anio * 365)
    mes = dias_total // 30
    dias_total = dias_total - (mes * 30)
    dia = dias_total
    edad = "Su edad es" + str(anio) +" años" + str(mes) +" meses y " + str(dia) + " días"
    return edad

print(calcular_edad(25,10,1993,4,8,2019))