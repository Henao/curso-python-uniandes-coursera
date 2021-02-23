# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:31:01 2021

@author: Henao
"""
def clasificar_regalo(id:int)->str:
    if id > 99 and id < 1000:
        if id%10 == id//100:
            palindromo = True
        else:
            palindromo = False
        if id % 2 == 0:
            par = True
        else:
            par = False
    if par == False and palindromo ==  True:
         respuesta = "girl"
    elif par == True and palindromo == True:
         respuesta = "boy"
    elif par == True and palindromo == False:
         respuesta = "man"
    else:
         respuesta = "woman"
    return respuesta
    print(str(respuesta))
    

