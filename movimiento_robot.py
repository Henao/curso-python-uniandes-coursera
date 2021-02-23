# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:08:25 2021

@author: Henao
"""
def movimiento_robot(orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str)->str:
      
    if orientacion_actual == "N" and giro_1 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_1 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_1 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_1 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_1 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_1 == "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_1 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_1 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_1 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_1 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_1 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_1 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_1 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_1 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_1 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_1 == ".":
        orientacion_actual = "S"
    
    orientacion_actual = orientacion_actual
    
    if orientacion_actual == "N" and giro_2 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_2 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_2 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_2 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_2 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_2== "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_2 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_2 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_2 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_2 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_2 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_2 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_2 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_2 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_2 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_2 == ".":
        orientacion_actual = "S"
    
    orientacion_actual  = orientacion_actual
    
    if orientacion_actual == "N" and giro_3 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_3 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_3 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_3 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_3 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_3 == "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_3 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_3 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_3 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_3 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_3 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_3 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_3 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_3 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_3 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_3 == ".":
        orientacion_actual = "S"
    
    return orientacion_actual
    
    
    

        
    
    
    
    