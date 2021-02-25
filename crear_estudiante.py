# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:28:49 2021

@author: Henao
"""
def crear_estudiante(nom:str, cod:str, gen:str, carr:str, prom:float, ssc:float)->dict:
    dic_estudiante = { "nombre": nom,
                       "código": cod,
                       "género": gen,
                       "carrera": carr,
                       "promedio": prom,
                       "ssc": ssc
                       }
    return dic_estudiante


#PROGRAMA PRINCIPAL
estudiante1 = crear_estudiante("Juan Pérez", "201824736", "masculino", "Biologia", 3.78, 0.7)
estudiante2 = crear_estudiante("Ana Guevara", "201845545", "femenino", "Ciencia Sociales", 3.89, 3.4)
estudiante3 = crear_estudiante("Bastien Bosa", "201985528", "masculino", "Matemáticas", 3.98, 1.7)
estudiante4 = crear_estudiante("Catalina Gomez", "202055586", "femenino", "Artes", 3.78, 4)

print("Los estudiantes son:\n", "Estudiante 1: \n", estudiante1,\
      "\nEstudiante 2:\n", estudiante2, \
      "\nEstudiante 3:\n", estudiante3, \
      "\nEstudiante 4:\n", estudiante4)
    
    