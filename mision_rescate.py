# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:56:06 2021

@author: Henao
"""
def mision_rescate(carga_sable: int, energia_escudo: int)->None:
    if not((carga_sable >= 90) and (energia_escudo >= 100)):
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta dejarte crujiente!")
    else:
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la princesa!")
        

def mision_rescate_v2(carga_sable: int, energia_escudo: int)->None:
    if (carga_sable < 90) or (energia_escudo < 100):
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta dejarte crujiente!")
    else:
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la princesa!")
        
        
def mision_rescate_v3(carga_sable: int, energia_escudo: int)->None:
    if (carga_sable >= 90) and (energia_escudo >= 100):
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la princesa!")
    else:
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta dejarte crujiente!")
        
        