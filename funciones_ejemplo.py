# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:29:34 2021

@author: Henao
"""
def funcion1()->str:
    return "hola como estas "

def funcion2(palabra:str)->str:
    return funcion1()+ str(palabra)

resultado= funcion2("juan")
print("El resultado de la función es: ", resultado)