# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:06:11 2021

@author: Henao
"""
def mayor_promedio(est1:dict, est2:dict, est3:dict, est4:dict)->dict:
    mayor_pro = est1
    
    if (est2["promedio"] >= mayor_pro["promedio"]):
        mayor_pro = est2
    if (est3["promedio"] >= mayor_pro["promedio"]):
        mayor_pro = est3
    if (est4["promedio"] >= mayor_pro["promedio"]):
        mayor_pro = est4
        
    return mayor_pro

est1 = {'nombre': 'Juan Pérez', 'código': '201824736', 'género': 'masculino', 'carrera': 'Biologia', 'promedio': 3.78, 'ssc': 0.7}
est2 = {'nombre': 'Ana Guevara', 'código': '201845545', 'género': 'femenino', 'carrera': 'Ciencia Sociales', 'promedio': 3.89, 'ssc': 3.4} 
est3 = {'nombre': 'Bastien Bosa', 'código': '201985528', 'género': 'masculino', 'carrera': 'Matemáticas', 'promedio': 3.98, 'ssc': 1.7} 
est4 = {'nombre': 'Catalina Gomez', 'código': '202055586', 'género': 'femenino', 'carrera': 'Artes', 'promedio': 3.78, 'ssc': 4}
mejor = mayor_promedio(est1, est2, est3, est4)

print("El estudiante de mayor promedio es:" + mejor["nombre"] + \
      "y su promedio es: " + str(mejor["promedio"]))