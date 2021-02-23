# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:55:40 2021

@author: Henao
"""

def pasaje_bogota_tokio(compania:str, edad:int, temporada_alta:bool, estudiante:bool)->int:
    precio = 5000000
    variaciones = 0
    seguro = False
    
    if compania == "ALAS":
        if temporada_alta: #Dejar solo temporada alta es como tener temporada_alta == True
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -=0.1
    
    elif compania == "VOLAR":
        if temporada_alta:
            variaciones += 0.2
        if edad > 60:
            seguro = True
    
    if edad < 18:
        variaciones -=0.5
        
    precio *= (1+variaciones)

    if seguro:
        precio += 100000 
        
    return round(precio)
#PROGRAMA PRINCIPAL
temp = bool(int(input("¿Es temporada alta? Ingrese 1 para SI y 0 para NO: ")))
compania = input("Ingrese el nombre de la compañia con la que viajará: ")
edad = int(input("Ingrese la edad de la presona: "))
estd = bool(int(input("¿Es estudiante? Ingrese 1 para SI y 0 para NO: ")))

tarifa = pasaje_bogota_tokio(compania, edad, temp, estd)
print("La tarifa del pasaje es de $" + str(tarifa) + " COP")