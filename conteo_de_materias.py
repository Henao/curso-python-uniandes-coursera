# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 07:18:43 2021

@author: Henao
"""

def conteo_de_materias(nombre_materia_1:str,nombre_materia_2:str,nombre_materia_3:str)->int:
    conteo = 0
    todas_materias = nombre_materia_1 +" "+nombre_materia_2+" "+nombre_materia_3
    
    if todas_materias.lower().count("matematica") > 0:
        conteo +=todas_materias.lower().count("matematica")
    if todas_materias.lower().count("programacion") > 0:
        conteo +=todas_materias.lower().count("programacion")
    if todas_materias.lower().count("filosofia") > 0:
       conteo +=todas_materias.lower().count("filosofia")     
    if todas_materias.lower().count("literatura") > 0:
       conteo +=todas_materias.lower().count("literatura")
        
        
    return conteo